using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using CareeriaIOTSensorControl.Models;

namespace CareeriaIOTSensorControl.Controllers
{
    public class CommandsController : Controller
    {
        private IoTDBEntities db = new IoTDBEntities();

        // GET: Commands
        public ActionResult Index()
        {
            return View(db.Commands.ToList());
        }

        public string GetCommand(int id)
        {
            string command = (from c in db.Commands
                              where (c.DeviceId == id) && (c.Executed == false)
                              select c.Command).FirstOrDefault();
            if (command == null)
                command = "";
            return command;
        }

        public string Completed(int id)
        {
            Commands command = (from c in db.Commands
                              where (c.DeviceId == id) && (c.Executed == false)
                              select c).FirstOrDefault();
            if (command != null)
            {
                command.Executed = true;
                db.SaveChanges();
            }
            return "Ok";
        }



        // GET: Commands/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Commands commands = db.Commands.Find(id);
            if (commands == null)
            {
                return HttpNotFound();
            }
            return View(commands);
        }

        // GET: Commands/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Commands/Create
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "Id_Command,DeviceId,Command")] Commands commands)
        {
            if (ModelState.IsValid)
            {
                db.Commands.Add(commands);
                commands.Executed = false;
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(commands);
        }

        // GET: Commands/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Commands commands = db.Commands.Find(id);
            if (commands == null)
            {
                return HttpNotFound();
            }
            return View(commands);
        }

        // POST: Commands/Edit/5
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "Id_Command,DeviceId,Command,Executed")] Commands commands)
        {
            if (ModelState.IsValid)
            {
                db.Entry(commands).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(commands);
        }

        // GET: Commands/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Commands commands = db.Commands.Find(id);
            if (commands == null)
            {
                return HttpNotFound();
            }
            return View(commands);
        }

        // POST: Commands/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            Commands commands = db.Commands.Find(id);
            db.Commands.Remove(commands);
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
