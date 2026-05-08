// KV: Kernel Version Utility
public static class KVTool {
    public static void ShowVersion() {
        string kernelType = "Star Kernel / Aura Kernel";
        string build = "v1.0.26-stable";
        
        Console.WriteLine("--------------------------------------");
        Console.WriteLine($"Kernel: {kernelType}");
        Console.WriteLine($"Build: {build}");
        Console.WriteLine($"Architecture: QuanticS (X86_64)");
        Console.WriteLine("Status: Protegido por Aura Super User");
        Console.WriteLine("--------------------------------------");
    }
}
