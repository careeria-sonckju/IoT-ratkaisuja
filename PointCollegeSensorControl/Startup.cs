using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(CareeriaIOTSensorControl.Startup))]
namespace CareeriaIOTSensorControl
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
