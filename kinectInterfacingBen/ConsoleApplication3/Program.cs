using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ConsoleApplication3
{
    class Program
    {
        public static bool end = false;
        static void Main(string[] args)
        {
            KinectControl a = new KinectControl();
            bool done = false;
            while (done == false)
            {
               
                done = end;
            }
                        
        }




        private void FormMain_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (char)Keys.Enter)
            {
                MessageBox.Show("e");
            }
        }
    }
}
