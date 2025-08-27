# upf

أداة لتصفية الروابط (URLs) وعرض الروابط الفريدة فقط حسب أسماء الباراميترات ونوعها.

---

## طريقة الاستخدام

### جميع الروابط
```bash
cat filename.txt | python upf.py | tee upf.txt
```

### فقط الروابط التي تحتوي باراميترات

```bash
cat filename.txt | python upf.py -p | tee upf.txt
```
