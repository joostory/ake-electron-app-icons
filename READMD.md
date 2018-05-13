# make electron app icons

png파일로 Electron app에서 사용하는 아이콘을 생성한다.

```
$ ./make-electron-app-icons.py --help
Usage: make-electron-app-icons.py [options] source_image

Options:
  -h, --help       show this help message and exit
  --output=OUTPUT  output dir

```

## 필요사항

ICNS를 생성하기 위해서 `png2icns`를 사용한다. `/usr/bin/png2icns`를 사용하니 이 위치에 없다면 스크립트를 수정하거나 이 위치에 png2icns를 복사해야한다.
