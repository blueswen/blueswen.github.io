import os

from material.plugins.blog.plugin import BlogPlugin
from material.plugins.blog.structure import Excerpt, View
from material.plugins.blog.structure.markdown import ExcerptTreeprocessor
from mkdocs.exceptions import PluginError
from mkdocs.plugins import event_priority
from mkdocs.structure.pages import Page
from mkdocs.structure.toc import get_toc


class CustomExcerpt(Excerpt):
    def render(self, page: Page, separator: str):
        self.file.url = page.url

        # Retrieve excerpt tree processor and set page as base
        at = self.md.treeprocessors.get_index_for_name("excerpt")
        processor: ExcerptTreeprocessor = self.md.treeprocessors[at]
        processor.base = page

        # Ensure that the excerpt includes a title in its content, since the
        # title is linked to the post when rendering - see https://t.ly/5Gg2F
        # self.markdown = self.post.markdown
        # if not self.post._title_from_render:
        #     self.markdown = "\n\n".join([f"# {self.post.title}", self.markdown])

        # Convert Markdown to HTML and extract excerpt
        # self.content = self.md.convert(self.markdown)
        # self.content, *_ = self.content.split(separator, 1)
        self.content = self.md.convert(f"# {self.post.title}")

        # Extract table of contents and reset post URL - if we wouldn't reset
        # the excerpt URL, linking to the excerpt from the view would not work
        self.toc = get_toc(getattr(self.md, "toc_tokens", []))
        self.file.url = self.post.url


class BlogExtensionPlugin(BlogPlugin):
    config_scheme = ()

    @event_priority(-50)
    def on_page_markdown(self, markdown, *, page, config, files):
        if not self.config.enabled:
            return

        # Skip if page is not a post managed by this instance - this plugin has
        # support for multiple instances, which is why this check is necessary
        if page not in self.blog.posts:
            if not self._config_pagination(page):
                return

            # We set the contents of the view to its title if pagination should
            # not keep the content of the original view on paginated views
            if not self.config.pagination_keep_content:
                view = self._resolve_original(page)
                if view in self._resolve_views(self.blog):
                    # If the current view is paginated, use the rendered title
                    # of the original view in case the author set the title in
                    # the page's contents, or it would be overridden with the
                    # one set in mkdocs.yml, leading to inconsistent headings
                    assert isinstance(view, View)
                    if view != page:
                        name = view._title_from_render or view.title
                        return f"# {name}"

            # Nothing more to be done for views
            return

        # Extract and assign authors to post, if enabled
        if self.config.authors:
            for name in page.config.authors:
                if name not in self.authors:
                    raise PluginError(f"Couldn't find author '{name}'")

                # Append to list of authors
                page.authors.append(self.authors[name])

        # Extract settings for excerpts
        separator = self.config.post_excerpt_separator
        max_authors = self.config.post_excerpt_max_authors
        max_categories = self.config.post_excerpt_max_categories

        # Ensure presence of separator and throw, if its absent and required -
        # we append the separator to the end of the contents of the post, if it
        # is not already present, so we can remove footnotes or other content
        # from the excerpt without affecting the content of the excerpt
        if separator not in page.markdown:
            if self.config.post_excerpt == "required":
                docs = os.path.relpath(config.docs_dir)
                path = os.path.relpath(page.file.abs_src_path, docs)
                raise PluginError(
                    f"Couldn't find '{separator}' in post '{path}' in '{docs}'"
                )
            else:
                page.markdown += f"\n\n{separator}"

        # Create excerpt for post and inherit authors and categories - excerpts
        # can contain a subset of the authors and categories of the post
        page.excerpt = CustomExcerpt(page, config, files)
        page.excerpt.authors = page.authors[:max_authors]
        page.excerpt.categories = page.categories[:max_categories]
