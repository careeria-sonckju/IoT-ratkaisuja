using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace CareeriaIOTSensorControl.ViewModels
{
    public class DeviceCommands
    {
        public int Id_Command { get; set; }
        public int DeviceId { get; set; }
        public string Command { get; set; }
        public Nullable<bool> Executed { get; set; }
    }
}