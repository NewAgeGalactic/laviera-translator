using System.Windows;

namespace HelpWindows
{
    public partial class HelpWindow : Window
    {
        public HelpWindow(string helpContent)
        {
            InitializeComponent();
            HelpTextBlock.Text = helpContent;
        }
    }
}
