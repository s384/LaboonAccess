# -*- mode: python -*-

block_cipher = None


a = Analysis(['run.py'],
             pathex=['/media/seba/Datos_Peques/Python/Mios/LaboonAccess'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [("./new_main.py", "new_main.py", "DATA")]
a.datas += [("./new_maing.py", "new_maing.py", "DATA")]
a.datas += [("./nosotros.py", "nosotros.py", "DATA")]
a.datas += [("./icons/minus-circle.svg", "icons/minus-circle.svg", "DATA")]
a.datas += [("./icons/minus-circle.svg", "icons/minus-circle.svg", "DATA")]
a.datas += [("./icons/parental.svg", "icons/parental.svg", "DATA")]
a.datas += [("./icons/plus-circle.svg", "icons/plus-circle.svg", "DATA")]
a.datas += [("./icons/save.svg", "icons/save.svg", "DATA")]
a.datas += [("./icons/sunrise.svg", "icons/sunrise.svg", "DATA")]
a.datas += [("./icons/sunset.svg", "icons/sunset.svg", "DATA")]
a.datas += [("./icons/user.svg", "icons/user.svg", "DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='LaboonAccess',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
