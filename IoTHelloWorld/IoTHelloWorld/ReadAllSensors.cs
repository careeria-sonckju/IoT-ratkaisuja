using Emmellsoft.IoT.Rpi.SenseHat;
using System;
using System.Diagnostics;
using System.Text;
using IoTHelloWorld;

namespace RPi.SenseHat.Demo.Demos
{
    public sealed class ReadAllSensors : SenseHatDemo
    {
        private Action<string> SetScreenText;
        public ReadAllSensors(ISenseHat senseHat, MainPage mainPage, 
            Action<string> setScreenText)
            : base(senseHat, mainPage)
        {
            this.SetScreenText = setScreenText;
        }

        public override void Run()
        {
            TimeSpan mainPageUpdateRate = TimeSpan.FromSeconds(0.5);
            DateTime nextMainPageUpdate = DateTime.Now.Add(mainPageUpdateRate);

            var stringBuilder = new StringBuilder();

            while (true)
            {
                Sleep(TimeSpan.FromMilliseconds(500));

                SenseHat.Sensors.ImuSensor.Update();      // Try get a new read-out for the Gyro, Acceleration, MagneticField and Pose.
                SenseHat.Sensors.PressureSensor.Update(); // Try get a new read-out for the Pressure.
                SenseHat.Sensors.HumiditySensor.Update(); // Try get a new read-out for the Temperature and Humidity.

                // Build up the string
                stringBuilder.Clear();
                stringBuilder.AppendLine($"Gyro: {SenseHat.Sensors.Gyro?.ToString(false) ?? "N/A"}");          // From the ImuSensor.
                stringBuilder.AppendLine($"Accel: {SenseHat.Sensors.Acceleration?.ToString(false) ?? "N/A"}"); // From the ImuSensor.
                stringBuilder.AppendLine($"Mag: {SenseHat.Sensors.MagneticField?.ToString(false) ?? "N/A"}");  // From the ImuSensor.
                stringBuilder.AppendLine($"Pose: {SenseHat.Sensors.Pose?.ToString(false) ?? "N/A"}");          // From the ImuSensor.
                stringBuilder.AppendLine($"Press: {SenseHat.Sensors.Pressure?.ToString() ?? "N/A"}");          // From the PressureSensor.
                stringBuilder.AppendLine($"Temp: {SenseHat.Sensors.Temperature?.ToString() ?? "N/A"}");        // From the HumiditySensor.
                stringBuilder.AppendLine($"Hum: {SenseHat.Sensors.Humidity?.ToString() ?? "N/A"}");            // From the HumiditySensor.

                if ((SetScreenText != null) && nextMainPageUpdate <= DateTime.Now)
                {
                    SetScreenText(stringBuilder.ToString());
                    nextMainPageUpdate = DateTime.Now.Add(mainPageUpdateRate);
                }

                Debug.WriteLine(stringBuilder.ToString());
            }
        }
    }
}