"""
Setup and installation for the package.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="moment",
    version="0.8.2",
    url="http://github.com/zachwill/moment",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    description="Dealing with dates and times should be easy",
    keywords=["moment", "dates", "times", "zachwill"],
    packages=[
        "moment"
    ],
    install_requires=[
        "dateparser>=0.6",
        "pytz>=2017.2",
        "times",
    ],
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
    ],
)
