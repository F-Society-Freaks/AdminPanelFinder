# Created by LimerBoy
# https://github.com/LimerBoy/AdminPanelFinder


# Signature class
class Signature:
    def __init__(self, name, atype, paths, signatures):
        self.name = name
        self.type = atype
        self.paths = paths
        self.signatures = signatures

# Signatures list
Signatures = [
    Signature("Azorult", "Stealer", ["/panel/admin.php"], ["<input type=\"submit\" value=\">>\">"]),
    Signature("BlackNet", "Botnet", ["/login.php", "/blacknet/login.php", "/BlackNET Panel/login.php"], ["BlackNET - Login", "Black.Hacker"]),
    Signature("Predator The Thief", "Stealer", ["/login"], ["<script>        $(function() {            $(\'.page-center\').matchHeight({                target: $(\'html\')            });            $(window).resize(function(){                setTimeout(function(){                    $(\'.page-center\').matchHeight({ remove: true });                    $(\'.page-center\').matchHeight({                        target: $(\'html\')                    });                },100);            });            $(\'.page-center\').css(\'display\', \'table\');        });", "Predator"]),
    Signature("Nexus", "Stealer", ["/"], ["<form action=\"#\" method=\"post\">                <div class=\"form-group\">                  <label class=\"label\">username</label>                  <div class=\"input-group\">                    <input type=\"text\" class=\"form-control\" name=\"username\" placeholder=\"username\">                    <div class=\"input-group-append\">                      <span class=\"input-group-text\"><i class=\"icon-check\"></i></span>                    </div>                  </div>                </div>                <div class=\"form-group\">                  <label class=\"label\">password</label>                  <div class=\"input-group\">                    <input type=\"password\" name=\"password\" class=\"form-control\" placeholder=\"*********\">                    <div class=\"input-group-append\">                      <span class=\"input-group-text\"><i class=\"icon-check\"></i></span>                    </div>                  </div>                </div>                <div class=\"form-group\">                  <button class=\"btn btn-primary submit-btn btn-block\">login</button>                </div>\t\t\t\t<div class=\"text-right\">\t\t\t\t<label class=\"switch mt-2\">\t\t\t\t\t<input type=\"checkbox\" onchange=\"nightmode()\" id=\"nmode\"><span class=\"slider\"></span>\t\t\t\t\t</label><label class=\"label ml-2\">nightmode</label>              </form>"]),
    Signature("Oski", "Stealer", ["/login.php"], ["<img src=\"template/img/img15.png\" class=\"img-fluid\" alt=\"\">            </div>          </div>          <div class=\"sign-wrapper mg-lg-l-50 mg-xl-l-60\">\t\t  <form method=\"post\">            <div class=\"wd-100p\">              <h3 class=\"tx-color-01 mg-b-5\">sign in</h3>              <p class=\"tx-color-03 tx-16 mg-b-40\">welcome back! please signin to continue.</p>              <div class=\"form-group\">                <label>login</label>                <input name=\"login\" type=\"text\" class=\"form-control\" placeholder=\"enter your login\">              </div>              <div class=\"form-group\">                <div class=\"d-flex justify-content-between mg-b-5\">                  <label class=\"mg-b-0-f\">password</label>                </div>                <input name=\"password\" type=\"password\" class=\"form-control\" placeholder=\"enter your password\">              </div>              <button type=\"submit\" class=\"btn btn-brand-02 btn-block\">sign in</button>            </div>\t\t\t</form>"]),
    Signature("Taurus", "Stealer", ["/"], ["<title>taurus</title>"]),
    Signature("Login Page", "Web Page", ["/login", "login.php"], ["<html>"]),
]