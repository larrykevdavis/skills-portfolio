<?php
include('./../assets/php/controller.php');

?>
<html lang="en" data-bs-theme="light">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Reviews - Employee Manager</title>
  <!--favicon-->
	<link rel="icon" href="../assets/images/favicon-32x32.png" type="image/png">

  <!--plugins-->
  <link href="../assets/plugins/perfect-scrollbar/css/perfect-scrollbar.css" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="../assets/plugins/metismenu/metisMenu.min.css">
  <link rel="stylesheet" type="text/css" href="../assets/plugins/metismenu/mm-vertical.css">
  <link rel="stylesheet" type="text/css" href="../assets/plugins/simplebar/css/simplebar.css">

  <!--bootstrap css-->
  <link href="../assets/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Material+Icons+Outlined" rel="stylesheet">
  <!--main css-->
  <link href="../assets/css/bootstrap-extended.css" rel="stylesheet">
  <link href="../sass/main.css" rel="stylesheet">
  <link href="../sass/dark-theme.css" rel="stylesheet">
  <link href="../sass/blue-theme.css" rel="stylesheet">
  <link href="../sass/semi-dark.css" rel="stylesheet">
  <link href="../sass/bordered-theme.css" rel="stylesheet">
  <link href="../sass/responsive.css" rel="stylesheet">

</head>

<body>

  <!--start header-->
<header class="top-header">
    <nav class="navbar navbar-expand align-items-center gap-4">
      <div class="btn-toggle">
        <a href="javascript:;"><i class="material-icons-outlined">menu</i></a>
      </div>
      <div class="search-bar flex-grow-1">
      
      </div>
      <ul class="navbar-nav gap-1 nav-right-links align-items-center">

        <li class="nav-item dropdown">
          <a href="javascrpt:;" class="dropdown-toggle dropdown-toggle-nocaret" data-bs-toggle="dropdown">
             <img src="assets/images/avatars/01.png" class="rounded-circle p-1 border" width="45" height="45" alt="">
          </a>
          <div class="dropdown-menu dropdown-user dropdown-menu-end shadow">
            <hr class="dropdown-divider">
            <a class="dropdown-item d-flex align-items-center gap-2 py-2" href="../logout"><i
            class="material-icons-outlined">power_settings_new</i>Logout</a>
          </div>
        </li>
      </ul>

    </nav>
  </header>
  <!--end top header-->

<!--start sidebar-->
   <aside class="sidebar-wrapper" data-simplebar="true">
    <div class="sidebar-header">
      <div class="logo-name flex-grow-1">
        <h6 class="mb-0">Employee Manager</h6>
      </div>
      <div class="sidebar-close">
        <span class="material-icons-outlined">close</span>
      </div>
    </div>
    <div class="sidebar-nav">
        <!--navigation-->
        <ul class="metismenu" id="sidenav">
          <li  class="active">
            <a href="../">
              <div class="parent-icon"><i class="material-icons-outlined">home</i>
              </div>
              <div class="menu-title">Dashboard</div>
            </a>
          </li>
        
          <li>
            <a href="../profile">
              <div class="parent-icon"><i class="material-icons-outlined">person</i>
              </div>
              <div class="menu-title">User Profile</div>
            </a>
          </li>


          <li>
            <a href="javascript">
              <div class="parent-icon"><i class="material-icons-outlined">list</i>
              </div>
              <div class="menu-title">Reviews</div>
            </a>
          </li>
         
        
         </ul>
        <!--end navigation-->
    </div>
  </aside>
<!--end sidebar-->


  <!--start main wrapper-->
  <main class="main-wrapper">
    <div class="main-content">
      <!--breadcrumb-->
      <div class="page-breadcrumb d-none d-sm-flex align-items-center mb-3">
        <div class="breadcrumb-title pe-3">Tasks</div>
        <div class="ps-3">
          <nav aria-label="breadcrumb">
            <ol class="breadcrumb mb-0 p-0">
              <li class="breadcrumb-item"><a href="javascript:;"><i class="bx bx-home-alt"></i></a>
              </li>
              <li class="breadcrumb-item active" aria-current="page">Task Reviews</li>
            </ol>
          </nav>
        </div>
      </div>
      <!--end breadcrumb-->
      <div class="card mt-4">
        <div class="card-body">
          <h5 class="mb-3 fw-bold">Ratings & Reviews<span class="fw-light ms-2"></span></h5>
          <div class="product-table">
            <div class="table-responsive white-space-nowrap">
              <table class="table align-middle">
                <thead class="table-light">
                  <tr>
                    <th>Task Name</th>
                    <th>Rating</th>
                    <th>Review</th>
                    <th>Date Reviewed</th>
                  </tr>
                </thead>
                <tbody>
                </tbody>
                  <?php
                    $employeeID=$_SESSION['employeeID'];
                    echo populateReviewTableUser($employeeID);
                  ?>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>


    </div>
  </main>
  <!--end main wrapper-->



     <!--start footer-->
     <footer class="page-footer">
      <p class="mb-0">Copyright © 2025. All right reserved.</p>
    </footer>
    <!--top footer-->



  

 

  <!--bootstrap js-->
  <script src="../assets/js/bootstrap.bundle.min.js"></script>

  <!--plugins-->
  <script src="../assets/js/jquery.min.js"></script>
  <!--plugins-->
  <script src="../assets/plugins/perfect-scrollbar/js/perfect-scrollbar.js"></script>
  <script src="../assets/plugins/metismenu/metisMenu.min.js"></script>
  <script src="../assets/plugins/simplebar/js/simplebar.min.js"></script>
  <script src="../assets/js/main.js"></script>
  <script>
    new PerfectScrollbar(".customer-notes")
  </script>


</body>

</html>