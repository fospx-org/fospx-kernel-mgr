from setuptools import setup, find_packages

setup(
    name="fospx-kernel-mgr",
    version="0.1.1",
    description="Linux Custom Kernel/GRUB Manager",
    author="Barın Güzeldemirci",
    author_email="baringuzeldemir@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "simple-term-menu",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "fospx-kernel-mgr=fospx_kernel_mgr.cli.main:main",
            "fospx-kernel-mgr-gtk=fospx_kernel_mgr.gui.main:main",
        ]
    },
)
