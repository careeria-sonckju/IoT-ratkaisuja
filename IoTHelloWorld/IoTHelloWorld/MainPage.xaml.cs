using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using System.ServiceModel.Channels;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;
using Windows.UI.Core;

// The Blank Page item template is documented at https://go.microsoft.com/fwlink/?LinkId=402352&clcid=0x409

namespace IoTHelloWorld
{
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();
        }
        internal async void SetScreenText(string text)
        {

            await Dispatcher.RunAsync(CoreDispatcherPriority.Normal, () =>
            {
                message.Text = text;
            });

            //var ignored = Dispatcher.RunAsync(CoreDispatcherPriority.Normal, () =>
            //{
            //    message.Text = text;
            //});

        }
           
        private void BtnHello_Click(object sender, RoutedEventArgs e)
        {
            SetScreenText("Heijaa Porvoo!");
        }

        private void BtnSenseDemo1_Click(object sender, RoutedEventArgs e)
        {
            SetScreenText("Teen sensoridemonstraation");
            RPi.SenseHat.Demo.DemoRunner.Run(s => new 
                RPi.SenseHat.Demo.Demos.DiscoLights(s, this));
        }

        private void BtnSensorit_Click(object sender, RoutedEventArgs e)
        {
            SetScreenText("Kaikki sensorit peliin!");
            RPi.SenseHat.Demo.DemoRunner.Run(s => new
                RPi.SenseHat.Demo.Demos.ReadAllSensors(s, this, SetScreenText));
        }

        private void BtnSulje_Click(object sender, RoutedEventArgs e)
        {
            SetScreenText("Suljen sovelluksen");
            //CoreApplication.Exit();
            Application.Current.Exit();
        }

        private void BtnTextScroll_Click(object sender, RoutedEventArgs e)
        {
            //message.Text = TxtScroll.Text;
            RPi.SenseHat.Demo.DemoRunner.Run(s => new
                RPi.SenseHat.Demo.Demos.MultiColorScrollText(s, this, "Poo"));
        }
    }
}
