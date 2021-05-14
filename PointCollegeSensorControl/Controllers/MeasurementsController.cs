using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using CareeriaIOTSensorControl.Models;
using System.Globalization;

namespace CareeriaIOTSensorControl.Controllers
{
    //8.11.2016 Lisätty koodi, joka tallentaa tietokantaan:
    public class MeasurementsController : Controller
    {
        private IoTDBEntities db = new IoTDBEntities();

        public String Store(int id, string value, int? type)
        {
            measurements m = new measurements();
            m.sender = id;
            CultureInfo en = new CultureInfo("en-US");
            DateTime localDate = DateTime.Now;

            m.value = double.Parse(value, en);
            m.time = localDate;
            m.type = type ?? 1; //jos mittauksen tyyppi on annettu, käytetään sitä, muuten oletetaan type=1 (lämpötila)
            db.measurements.Add(m);
            db.SaveChanges();
            return "ok";
        } 

        // GET: Measurements
        public ActionResult Index()
        {
            var mittaukset = (from m in db.measurements
                              orderby m.time descending
                              select m).Take(500).ToList();
            return View(mittaukset);
        }

        // GET: Measurements/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            measurements measurements = db.measurements.Find(id);
            if (measurements == null)
            {
                return HttpNotFound();
            }
            return View(measurements);
        }

        // GET: Measurements/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Measurements/Create
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "id,sender,time,type,value")] measurements measurements)
        {
            if (ModelState.IsValid)
            {
                db.measurements.Add(measurements);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(measurements);
        }

        // GET: Measurements/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            measurements measurements = db.measurements.Find(id);
            if (measurements == null)
            {
                return HttpNotFound();
            }
            return View(measurements);
        }

        // POST: Measurements/Edit/5
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "id,sender,time,type,value")] measurements measurements)
        {
            if (ModelState.IsValid)
            {
                db.Entry(measurements).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(measurements);
        }

        // GET: Measurements/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            measurements measurements = db.measurements.Find(id);
            if (measurements == null)
            {
                return HttpNotFound();
            }
            return View(measurements);
        }

        // POST: Measurements/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            measurements measurements = db.measurements.Find(id);
            db.measurements.Remove(measurements);
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }
    }
}
