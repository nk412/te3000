https://nk412.com/te3000


```bash
curl https://nk412.com/te3000/| sed s/"\.html"/"\.html\n"/g | grep "\.html" | awk -F 'href' '{print $2}' | sed s/"=\""/"https:\/\/nk412.com\/te3000\/"/g
```
