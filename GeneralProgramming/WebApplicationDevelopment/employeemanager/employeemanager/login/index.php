<?php
include('../assets/php/controller.php')
?>
<html lang="en" data-bs-theme="light">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Login - Employee Manager</title>
  <!--favicon-->
	<link rel="icon" href="../assets/images/favicon-32x32.png" type="image/png">


  <!--plugins-->
  <link href="../assets/plugins/perfect-scrollbar/css/perfect-scrollbar.css" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="../assets/plugins/metismenu/metisMenu.min.css">
  <link rel="stylesheet" type="text/css" href="../assets/plugins/metismenu/mm-vertical.css">
  <!--bootstrap css-->
  <link href="../assets/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Material+Icons+Outlined" rel="stylesheet">
  <!--main css-->
  <link href="../assets/css/bootstrap-extended.css" rel="stylesheet">
  <link href="../sass/main.css" rel="stylesheet">
  <link href="../sass/dark-theme.css" rel="stylesheet">
  <link href="../sass/blue-theme.css" rel="stylesheet">
  <link href="../sass/responsive.css" rel="stylesheet">

  </head>

  <body>

    <!--authentication-->
    <div class="auth-basic-wrapper d-flex align-items-center justify-content-center">
      <div class="container-fluid my-5 my-lg-0">
        <div class="row">
           <div class="col-12 col-md-8 col-lg-6 col-xl-5 col-xxl-4 mx-auto">
            <div class="card rounded-4 mb-0 border-top border-4 border-primary border-gradient-1">
              <div class="card-body p-5">
                  <h4 class="fw-bold">Employee Manager</h4>
                  <p class="mb-0">Enter your credentials to login your account</p>

                  <div class="form-body my-5">

                     <p style="color:red;">
                      <?php

                      if(isset($_SESSION['login_err'])){
                        $_SESSION['login_suc']="";
                        echo $_SESSION['login_err'];
                      }
                      ?>
                    </p>
                     <p style="color:green;">
                      <?php
                      if(isset($_SESSION['login_suc'])){
                        echo $_SESSION['login_suc'];
                        $_SESSION['login_err']="";
                      }
                      ?>
                    </p>
										<form class="row g-3" method="POST">
											<div class="col-12">
												<label for="inputEmailAddress" class="form-label">Email</label>
												<input type="email" name="email" class="form-control" required placeholder="jhon@example.com">
											</div>
											<div class="col-12">
												<label for="inputChoosePassword" class="form-label">Password</label>
												<div class="input-group" id="show_hide_password">
													<input type="password" class="form-control border-end-0" name="password" placeholder="Enter Password"> 
                          <a href="javascript:;" class="input-group-text bg-transparent"><i class="bi bi-eye-slash-fill"></i></a>
												</div>
											</div>
									
											<div class="col-12">
												<div class="d-grid">
													<input type="submit" class="btn btn-grd-primary" value="Login" name="login">
												</div>
											</div>
											<div class="col-12">
												<div class="text-start">
													<p class="mb-0">Don't have an account yet? <a href="../register">Sign up here</a>
													</p>
												</div>
											</div>
										</form>
									</div>

              </div>
            </div>
           </div>
        </div><!--end row-->
     </div>
    </div>
    <!--authentication-->


    <!--plugins-->
    <script src="../assets/js/jquery.min.js"></script>

    <script>
      $(document).ready(function () {
        $("#show_hide_password a").on('click', function (event) {
          event.preventDefault();
          if ($('#show_hide_password input').attr("type") == "text") {
            $('#show_hide_password input').attr('type', 'password');
            $('#show_hide_password i').addClass("bi-eye-slash-fill");
            $('#show_hide_password i').removeClass("bi-eye-fill");
          } else if ($('#show_hide_password input').attr("type") == "password") {
            $('#show_hide_password input').attr('type', 'text');
            $('#show_hide_password i').removeClass("bi-eye-slash-fill");
            $('#show_hide_password i').addClass("bi-eye-fill");
          }
        });
      });
    </script>
  
  </body>
</html>