// LST: Logo Screen Time
public static class LST {
    public static void Display() {
        string logo = @"
   @@@@@@   @@@  @@@  @@@@@@@@    @@@@@@  
  @@@@@@@@  @@@  @@@  @@@@@@@@   @@@@@@@@ 
  @@!  @@@  @@!  @@@  @@!        @@!  @@@ 
  !@!  @!@  !@!  @!@  !@!        !@!  @!@ 
  @!@!@!@!  @!@  !@!  @!!!:!     @!@  !@! 
  !!!@!!!!  !@!  !!!  !!!!!:     !@!  !!! 
  !!:  !!!  !!:  !!!  !!:        !!:  !!! 
  :!:  !:!  :!:  !:!  :!:        :!:  !:! 
   ::   ::: ::::: ::   :: ::::   ::::: :: 
   :   : :   : :  :   : :: ::     : :  :  ";

        Console.ForegroundColor = ConsoleColor.Magenta;
        Console.WriteLine(logo);
        Console.ResetColor();

        Console.WriteLine("\n      AuraOS 1.0 ");
        Console.WriteLine("      ----------------------------");
        Console.WriteLine("      OS: AuraOS x86_64");
        Console.WriteLine("      Kernel: Star Kernel v1.0");
        Console.WriteLine("      Uptime: 42 mins");
        Console.WriteLine("      Packages: 154 (apm)");
        Console.WriteLine("      Shell: AuraShell v2.0");
        Console.WriteLine("      Edition: Test Edition ");
        Console.WriteLine("      Missão: Provando o potencial para o mundo.");
        Console.WriteLine();
    }
}
