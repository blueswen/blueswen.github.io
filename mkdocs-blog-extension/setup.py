from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mkdocs-blog-extension",
    version="0.3.5",
    author="Blueswen",
    author_email="blueswen.tw@gmail.com",
    keywords=["mkdocs", "plugin"],
    packages=find_packages(),
    license="MIT",
    description="MkDocs blog extension.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    entry_points={
        "mkdocs.plugins": [
            "blog-extension = mkdocs_blog_extension.plugin:BlogExtensionPlugin",
        ]
    },
)
