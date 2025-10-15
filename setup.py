from setuptools import setup
from setuptools.command.install import install
import os


class PostInstallCommand(install):
    def run(self):
        install.run(self)

        # .pth 檔案內容 - 使用模組導入方式
        pth_content = "import path_loader.auto_loader"

        # 取得 site-packages 目錄
        from distutils.sysconfig import get_python_lib

        site_packages = get_python_lib()
        pth_file = os.path.join(site_packages, "path_loader_auto.pth")

        try:
            with open(pth_file, "w", encoding="utf-8") as f:
                f.write(pth_content)
            print(f"\n✓ 成功建立自動載入設定: {pth_file}")
        except Exception as e:
            print(f"\n✗ 警告: 無法建立 .pth 檔案: {e}")


setup(
    cmdclass={
        "install": PostInstallCommand,
    },
)
