using System;
using System.IO.Ports;
using System.IO;
using System.Windows.Forms;
using System.Globalization;
using GMap.NET;

// This is the code for your desktop app.
// Press Ctrl+F5 (or go to Debug > Start Without Debugging) to run your app.

namespace missionControl1
{
    public partial class Form1 : Form
    {

        SerialPort mySerialPort = new SerialPort("COM7");
        string[] parsed;
        bool fix;
        bool save_flag = false;
        int file = 0;
        string csv = "manual_save";
        string manual_path;
        string[] ports;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            mySerialPort.BaudRate = 9600;
            mySerialPort.Parity = Parity.None;
            mySerialPort.StopBits = StopBits.One;
            mySerialPort.DataBits = 8;
            mySerialPort.Handshake = Handshake.None;
            mySerialPort.RtsEnable = true;
            
            mySerialPort.DataReceived += new SerialDataReceivedEventHandler(DataReceivedHandler);

            mySerialPort.Open();
            map.MapProvider = GMap.NET.MapProviders.BingMapProvider.Instance;
            map.MinZoom = 5;
            map.MaxZoom = 20;
            map.Zoom = 15;
            string header = "manual_saver\n";
            while (File.Exists(csv + file.ToString() + ".csv"))
            {
                file++;
            }
            manual_path = csv + file.ToString() + ".csv";
            File.WriteAllText(manual_path, header);
            ports = SerialPort.GetPortNames();
        }

        private void DataReceivedHandler(object sender, SerialDataReceivedEventArgs e)
        {
            SerialPort sp = (SerialPort)sender;
            string indata = sp.ReadExisting();
            if (save_flag)
            {
                File.AppendAllText(manual_path, indata);
            }
            this.Invoke((MethodInvoker)delegate
            {
                tb_raw.Text = indata;
            });
            parsed = parse_string(indata);
            update_text(parsed);
            sp.DiscardInBuffer();
        }

        private string[] parse_string(string input_data)
        {
            string[] alldat = input_data.Split(',');
            return alldat;
        }

        private void update_text(string[] dat_delim)
        {
            int equ;
            int mer;
            double lat = 0.0;
            double lon = 0.0;

            if (dat_delim.Length <= 1) return; // Checking for data
            if (dat_delim[4] == "") fix = false; // if the latitude string is empty there is no fix
            else fix = true;

            if (dat_delim[5] == "N") equ = 1;
            else equ = -1;

            if (dat_delim[7] == "E") mer = 1;
            else mer = -1;
            if (fix)
            {
                lat = Convert.ToDouble(get_geo(dat_delim[4])) * equ;
                lon = Convert.ToDouble(get_geo(dat_delim[6])) * mer;
            }
            // This will update all GUI elements whenever new data is received
            try
            {
                this.Invoke((MethodInvoker)delegate
                {
                    tb_lat.Text = lat.ToString();
                    tb_lon.Text = lon.ToString();
                    btn_fix.Checked = fix;
                    if (fix) map.Position = new PointLatLng(lat, lon);
                });
            }
            catch (System.InvalidOperationException)
            {
                // This happens when closing the GUI
            }
        }

        private string get_geo(string coord)
        {
            float geo = float.Parse(coord, CultureInfo.InvariantCulture.NumberFormat);
            int dd = (int)geo / 100;
            float ss = geo - (float)dd * 100;
            geo = dd + ss / 60;
            return geo.ToString("0.00000");
        }

        private void btn_data_save_Click(object sender, EventArgs e)
        {
            if (!save_flag) btn_data_save.Text = "Stop Saving";
            else btn_data_save.Text = "Start Saving";

            save_flag = !save_flag;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            //mySerialPort.PortName = 
        }
    }
}
