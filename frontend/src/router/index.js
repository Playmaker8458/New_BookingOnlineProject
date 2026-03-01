import { createRouter, createWebHistory } from 'vue-router'
import routes from './router'

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

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes
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