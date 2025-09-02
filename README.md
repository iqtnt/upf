# Upf

أداة بسيطة لتصفية الروابط (URLs) وعرض الروابط الفريدة فقط بناءً على أسماء الباراميترات ونوعها، مع إمكانية التصفية حسب الامتدادات.

---

## طريقة الاستخدام

### جميع الروابط
```bash
cat filename.txt | python upf.py | tee upf.txt
```

### فقط الروابط التي تحتوي على باراميترات

```bash
cat filename.txt | python upf.py -p | tee upf.txt
```

### تصفية الروابط حسب الامتداد (مثل php, js, css)

```bash
cat filename.txt | python upf.py -ext php,js,css | tee upf.txt
```
