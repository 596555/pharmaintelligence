# بيئة البحث العلمي المتصلة — دليل الربط

## 1. مصادر بيانات عامة قابلة للاستخدام البرمجي

| المصدر | الاستخدام داخل المختبر | نقطة الدخول |
|---|---|---|
| openFDA Drug Events / FAERS | استكشاف بلاغات السلامة الدوائية | https://open.fda.gov/apis/drug/event/ |
| openFDA Drug Label | استكشاف بيانات النشرات الدوائية الأمريكية | https://open.fda.gov/apis/drug/label/ |
| PubChem PUG REST | معرفات المركبات والخصائص الكيميائية | https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| RxNorm / RxNav | البحث في أسماء ومفاهيم الأدوية الأمريكية المعيارية | https://lhncbc.nlm.nih.gov/RxNav/APIs/ |
| ClinicalTrials.gov API | البحث في الدراسات السريرية وحالاتها | https://clinicaltrials.gov/data-api/about-api |
| DailyMed | نشرات الأدوية المقدمة إلى FDA | https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm |
| NCBI PubMed | الأدبيات الطبية الحيوية | https://pubmed.ncbi.nlm.nih.gov/ |

المصادر تختلف في النطاق الجغرافي والتغطية والتحديث والتراخيص. RxNorm وNDC بيانات أمريكية وليست قاموساً شاملاً مسجلاً في اليمن أو الخليج. openFDA يعرض بيانات عامة ولا ينبغي استخدامه لاتخاذ قرار علاجي. FAERS بلاغات تلقائية لا تثبت السببية ولا تحسب معدل حدوث.

## 2. موصلات برمجية جاهزة في المستودع

الأداة `08-RESEARCH-TOOLS/data_hub.py` تستخدم مكتبات Python القياسية فقط وتدعم:
- openFDA adverse event reports.
- openFDA product labeling.
- PubChem compound properties.
- RxNorm approximate name lookup.

من PowerShell داخل جذر المستودع:

```powershell
py 08-RESEARCH-TOOLS/data_hub.py pubchem aspirin
py 08-RESEARCH-TOOLS/data_hub.py rxnorm metformin
py 08-RESEARCH-TOOLS/data_hub.py openfda-label paracetamol --limit 5
py 08-RESEARCH-TOOLS/data_hub.py openfda-events aspirin --limit 5
```

النتائج تحفظ في `data/research_cache/` بصيغة JSON مع metadata: اسم المصدر، رابط الاستعلام، عبارة البحث، وقت الجلب UTC، وحدود الاستخدام. مجلد البيانات الخام المحلي مستثنى من Git.

لـ openFDA، يمكن استخدام API key مجاني اختيارياً عبر متغير البيئة `OPENFDA_API_KEY`. لا تضع المفتاح داخل الكود أو GitHub. من PowerShell للجلسة الحالية:
```powershell
$env:OPENFDA_API_KEY = "ضع_مفتاحك_هنا"
```
الموصل يعمل دون مفتاح وفق حدود الاستخدام المعلنة من FDA.

## 3. بيئة الأدوات

- **GitHub:** المصدر الرسمي للكود، Issues للمهام، Actions للاختبارات التلقائية، Releases للإصدارات.
- **VS Code:** تحرير وتشغيل Python وSQL محلياً.
- **Python + venv:** بيئة قابلة لإعادة الإنتاج.
- **Jupyter / Google Colab:** تجارب تحليلية ودفاتر تعليمية؛ لا ترفع بيانات سرية.
- **SQLite:** قاعدة بيانات محلية خفيفة للتدريب على جداول الأدوية والدفعات والصرف.
- **Streamlit:** واجهات منتجات المخزون والتحليل.
- **Kaggle Learn:** تمارين Python/SQL/Pandas مع شهادات إكمال مجانية.
- **IBM SkillsBuild:** تعلم بيانات وذكاء اصطناعي وشارات رقمية.

## 4. معايير النزاهة العلمية وجودة البيانات

كل ملف بيانات مستورد يجب أن يسجل:
1. المصدر والرابط وتاريخ الاستخراج.
2. تعريف الحقول والوحدات واللغة والبلد.
3. تاريخ التحديث أو الإصدار إن توفر.
4. الترخيص وشروط إعادة الاستخدام.
5. التحويلات والتنظيف وإزالة التكرار.
6. القيود والانحيازات والبيانات المفقودة.

لا تخلط بين generic name وbrand name وingredient، ولا بين strength وdose وpack size. لا تدمج المنتجات بناءً على تشابه الاسم فقط. لا تخلط العبوات والوحدات في تحليل الاستهلاك.

## 5. قواعد الاستخدام الآمن

- استخدم بيانات اصطناعية أو عامة أو بيانات لديك إذن مكتوب باستخدامها.
- لا ترفع ملفات المرضى أو سجلات الصيدليات/المصانع الخاصة إلى GitHub أو خدمات خارجية.
- لا تعتمد بيانات FDA الأمريكية بديلاً عن النشرة المعتمدة محلياً.
- لا تحول نتائج البحث إلى نصيحة علاجية أو قرار شراء أو إطلاق دفعة.
- لا تستخدم FAERS أو ROR/PRR لإثبات السببية أو incidence.
- لا تستخدم خصائص PubChem أو تنبؤات QSAR/docking لإثبات الفعالية أو السلامة.
- احترم حدود الطلبات ومعدلات الاستخدام لكل API؛ لا تنفذ مسحاً كثيفاً دون مراجعة شروط المصدر.

## 6. ما لا يدعي المشروع أنه متصل به

لا توجد حالياً مزامنة تلقائية مع أنظمة صيدلية أو مصنع أو سجلات مرضى أو WHO VigiBase أو MedDRA أو WHODrug؛ هذه موارد مقيدة أو تجارية أو تتطلب صلاحيات. الربط المذكور هنا مع APIs العامة فقط.
