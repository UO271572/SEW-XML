   M S B A M L   `   `   `  ????F  BXAMLProyect, Version=1.0.0.0, Culture=neutral, PublicKeyToken=nullG(clr-namespace:XAMLProyect.MVVM.ViewModelXAMLProyect.MVVM.ViewModel  5   	   )clr-namespace:XAMLProyectXAMLProyect  5   	       XAMLProyect.MainWindow   5   	   R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   >	viewModel(clr-namespace:XAMLProyect.MVVM.ViewModel     5   	   +localclr-namespace:XAMLProyect     5   	     ? Title$  
MainWindow??5	   	   $	??500??5
   	   $	??800??6    ? WindowStyle$
 None=?5   	    ? 
ResizeMode$ NoResize=?5   	   
??????  ? AllowsTransparency .  ? DataContext 5      .  (XAMLProyect.MVVM.ViewModel.MainViewModel  5   
   .??5      ?? ???#272535 ?? CornerRadius$ 30??6"   ._?5   
   ?  ? ColumnDefinitions 5      ?? 5      $	??250 ?6#   ?? 5       ? RowDefinitions 5      ?? 5      $??75 ?6    ?? 5      .+?5!      ?? $	??HBO??6   $??Center=?5"      $??Center=?5#      
???????$??34(?5%         HBOhead#??[  5&      ?? 5)      $??1??6   .+?5+      	? $??	Peliculas??6   $??50??5,      
???????$??16(?5.        MenuButtonTheme#??[ 5/      	? 50      $??Series??6   $??50??51      
???????$??16(?53      #??[ 54      	? 55      $??Tendencias ahora??6   $??50??56      
???????$??16(?58      #??[ 59      5<      ?? 5>      $
??auto??6   $??50??6#   $??Stretch=?5?      $??Stretch=?5@      $??1??5A      $??	30,0,30,0q?5B        
BrowserBox#??[ 5C      ?? 5E      $??1??6   $??1??5F      $??30q?5G      ??5H      ?? *CurrentView+5J      5L      5M      