$port = 445
$net = read-host “where we are going ? 192.168.0”
$range = 90..100
$result = New-Item -type file ".\result.txt" -Force


foreach ($r in $range)
{
   $ip = “{0}.{1}” -F $net,$r
    if(Test-Connection -BufferSize 32 -Count 1 -Quiet -ComputerName $ip){
 	   $socket = new-object System.Net.Sockets.TcpClient($ip, $port)
 	   if($socket.Connected){
            $dic = Get-Content ".\dic.txt"
            foreach ($share in $dic)
            {
                try
                {
                    Get-ChildItem -Path "\\$ip\$share"
                    write-host "[+] Read access to share \\$ip\\$share" -ForegroundColor Yellow -BackgroundColor DarkCyan
                    write-host "[+] Read access to share \\$ip\\$share" >> $result
                }
                catch{write-host "[-] No access to share \\$ip\\$share" -ForegroundColor Red -BackgroundColor Black}
            }
    	     $socket.Close()}
         }
 }
