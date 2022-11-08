using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using XAMLProyect.Core;

namespace XAMLProyect.MVVM.ViewModel
{
    class MainViewModel:ObservableObject
    {

        private object _currentView;
        public object CurrentView { 
            get { return _currentView; }
            set { _currentView = value;
                OnPropertyChanged();
                    }
        }
        public HomeViewModel HomeView { set; get; }

        public MainViewModel()
        {
            HomeView = new HomeViewModel();
            _currentView = HomeView;
        }
    }
}
