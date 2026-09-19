/**
 * Google Apps Script - استقبال درجات الطلاب وكتابتها في Google Sheet
 * ----------------------------------------------------------------------
 * الربط بجدول البيانات:
 *   https://docs.google.com/spreadsheets/d/1tJ-C1IJZrsh9hYDtp_mGuyt9jySZc_zJmJ5fftmvbgU/edit
 *
 * خطوات التركيب:
 *   1) افتح جدول البيانات ثم: الإضافات (Extensions) < Apps Script.
 *   2) احذف أي كود موجود والصق هذا الكود بالكامل، ثم احفظ.
 *   3) Deploy < New deployment < Type: Web app.
 *        - Execute as: Me (أنت)
 *        - Who has access: Anyone
 *      ثم Deploy وامنح الأذونات المطلوبة.
 *   4) انسخ رابط الـ Web app URL (يt.google.com/macros/s/AKfycbwH3FghQxQ2Nvl6fm6ehhgkUQC815PBJ6VWlcoiYiqtYkrVlGES8-sdw2-P3Udg_Wedqg/exec)
 *      وضعه في إعداد SHEET_WEBAPP.webAppUrl داخل ملف الورقة (HTML).
 */

var SHEET_ID = '1tJ-C1IJZrsh9hYDtp_mGuyt9jySZc_zJmJ5fftmvbgU';
var SHEET_NAME = 'الدرجات'; // اسم التبويب الذي ستُكتب فيه الدرجات
var HEADERS = ['الوقت', 'اسم الطالب', 'الفصل', 'الدرجة', 'الدرجة الكلية', 'النسبة %', 'إجابات صحيحة', 'إجابات خاطئة'];

function doPost(e) {
  try {
    var ss = SpreadsheetApp.openById(SHEET_ID);
    var sheet = ss.getSheetByName(SHEET_NAME);
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      sheet.appendRow(HEADERS);
    }
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(HEADERS);
    }
    var p = (e && e.parameter) ? e.parameter : {};
    sheet.appendRow([
      new Date(),
      p.name || '',
      p.section || '',
      p.score || '',
      p.total || '',
      p.percentage || '',
      p.correct || '',
      p.incorrect || ''
    ]);
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok' }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet() {
  return ContentService
    .createTextOutput('Quiz results endpoint is running.')
    .setMimeType(ContentService.MimeType.TEXT);
}
