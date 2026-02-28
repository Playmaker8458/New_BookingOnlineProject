// หน้่าเพจหลัก
import landingpage from '../page/landingpage.vue'

// layout
import AdminLayout from '../layout/AdminLayout.vue'
import StudentLayout from '../layout/StudentLayout.vue'

// หน้า Login ของผู้ดูแลระบบ และผู้ใช้ทั้ง 2 กลุ่ม
import LoginAdmin from '../page/LoginAdmin.vue'
import LoginUser from '../page/LoginUser.vue'

// หน้าเพจของผู้ดูแลระบบทั้งหมด
import HomepageAdmin from '../page/AdminPage/Homepage.vue'
import LoginRights from '../page/AdminPage/LoginRights.vue'
import ManageUserAccounts from '../page/AdminPage/ManageUserAccounts.vue'

// หน้าเพจของนักศึกษาทั้งหมด
import HomepageStudent from '../page/StudentPage/Homepage.vue'
import BookAppointment from '../page/StudentPage/BookAppointment.vue'

import { createRouter, createWebHistory } from 'vue-router'

//  ฟังก์ชันตรวจสอบ access_token
function checkToken() {
  const access_token = localStorage.getItem("access_token");
  const expiresAt = localStorage.getItem("expiresAt");

  if (!access_token || !expiresAt) return false;

  if (Date.now() > Number(expiresAt)) {
    localStorage.removeItem("access_token");
    localStorage.removeItem("expiresAt");
    return false;
  }

  return true; 
}

const routes = [
  {
    path: '/',
    name: 'landingpage',
    component: landingpage
  },

  {
    path: '/admin',
    component: AdminLayout,
    children: [
      { path: 'loginadmin', name: "loginadmin", component: LoginAdmin },
      { 
        path: 'homepageAdmin', 
        name: "homepageAdmin", 
        component: HomepageAdmin,
        meta: { requiresAuth: true }
      },
      { path: 'loginrights', name: "loginrights", component: LoginRights },
      { path: 'manageuseraccounts', name: "manageuseraccounts", component: ManageUserAccounts, meta: { requiresAuth: true } }
    ]
  },

  {
    path: '/loginuser',
    name: 'LoginUser',
    component: LoginUser
  },

  {
    path: '/student',
    component:StudentLayout,
    children: [
      {
        path: 'homepage',
        name: 'HomepageStudent',
        component: HomepageStudent
      },
      {
        path: 'book-appointment',
        name: 'BookAppointment',
        component: BookAppointment
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})


//  ตรวจสอบก่อนเข้า route
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !checkToken()) {
    next("/admin/loginadmin");
  } else {
    next();
  }
})

export default router