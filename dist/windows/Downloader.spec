# -*- mode: python -*-

block_cipher = None


a = Analysis(['Downloader.py'],
             pathex=['Y:\\1985\\python\\Build'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Downloader',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='Y:\\1985\\python\\Build\\icons\\app.ico')
