# GetPixelColor

## A cross-platform python library for getting the color of a given pixel on screen.
## **origin by 9021007**


 - Compatible with MacOS arm64, Windows, and Linux.
 - Transparency data only available on some platforms.
   
__Examples:__

Make sure you first `import getpixelcolor`

Get color of a specific pixel: `getpixelcolor.pixel(x, y)`

> (R, G, B, (A))

Get average color of an area: `getpixelcolor.average(x, y, width, height)`

> (R, G, B, (A))

Get all color values of an area: `getpixelcolor.area(x, y, width, height)`

> [[[R, G, B, (A)]]]
