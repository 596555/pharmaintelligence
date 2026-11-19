# نشر PHARMAINTELLIGENCE Web Lab على المتصفح

## الحالة
واجهة المختبر موجودة في `13-WEB-LAB/` وتُفحص صياغة JavaScript تلقائياً. نشر GitHub Pages يحتاج تفعيل مصدر النشر مرة واحدة من إعدادات المستودع؛ محاولة التفعيل التلقائي من GitHub Actions رُفضت لأن رمز التشغيل لا يملك صلاحية إنشاء موقع Pages في هذا المستودع.

## التفعيل الأول مرة واحدة
1. افتح: https://github.com/596555/pharmaintelligence/settings/pages
2. في **Build and deployment** اختر **GitHub Actions** من **Source**.
3. احفظ الإعداد إن ظهر زر حفظ.
4. افتح تبويب Actions وشغّل **Deploy PHARMAINTELLIGENCE Web Lab** باستخدام **Run workflow** على فرع `main`، أو اطلب إعادة تشغيل المهمة بعد تفعيل Pages.
5. بعد نجاح خطوة Deploy to GitHub Pages افتح:
   https://596555.github.io/pharmaintelligence/

## التحقق
- Workflow: `.github/workflows/deploy-web-lab.yml`
- يفحص `node --check 13-WEB-LAB/app.js` ثم يرفع محتويات `13-WEB-LAB/` وينشرها.
- راقب رابط النشر في تبويب Actions أو Settings → Pages.

## متطلبات المتصفح والإنترنت
- استخدم إصداراً حديثاً من Chrome أو Edge أو Firefox.
- يحتاج Python runtime وExcel reader وSQLite engine إلى تنزيل مكتباتها من CDN عند الاستخدام الأول.
- قد تحتاج واجهات PubChem وRxNorm وopenFDA إلى الوصول المباشر إلى الإنترنت؛ بعض الشبكات قد تمنع بعض النطاقات أو طلبات CORS.
- Python يعمل داخل WebAssembly عبر Pyodide، وليس Python سطح المكتب؛ ليست كل الحزم أو صلاحيات نظام الملفات متاحة.
- مختبر الجداول يوفر وظائف أساسية لفتح CSV/XLSX وتحرير الخلايا وتصدير XLSX، وليس بديلاً كاملاً عن Excel Desktop.
- SQL يعمل بمحرك SQLite داخل ذاكرة الصفحة، وتُفقد قاعدة التدريب المؤقتة عند إعادة تحميل الصفحة.

## الخصوصية والسلامة
الملفات والجداول تُعالج محلياً في المتصفح ولا تُرفع بواسطة وظائف المختبر. لا تدخل بيانات مرضى أو بيانات تجارية سرية. نتائج قواعد البيانات العامة أدوات بحث وتعلم، وليست توجيهاً علاجياً أو قراراً تنظيمياً.
