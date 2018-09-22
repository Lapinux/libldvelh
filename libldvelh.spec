# -*- mode: python -*-

block_cipher = None

a = Analysis(['libldvelh.py'],
             pathex=['C:\\Users\\arthur\\Desktop\\essai python\\bib'],
             binaries=[],
             datas=[
			( 'setting/*.dat', 'setting' ),
			( 'scenes/*.csv', 'scenes' )
			],
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
          exclude_binaries=True,
          name='libldvelh',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='libldvelh')
