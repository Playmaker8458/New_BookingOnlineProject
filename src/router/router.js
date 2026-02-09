// หน้่าเพจหลัก
import landingpage from '../page/landingpage.vue'

// หน้า Login ของผู้ดูแลระบบ และผู้ใช้ทั้ง 2 กลุ่ม [นักศึกษา และ อาจารย์]
import LoginAdmin from '../page/LoginAdmin.vue'
import LoginUser from '../page/LoginUser.vue'

// หน้าเพจของผู้ดูแลระบบทั้งหมด
import HomepageAdmin from '../page/AdminPage/Homepage.vue'
import LoginRights from '../page/AdminPage/LoginRights.vue'
import ManageUserAccounts from '../page/AdminPage/ManageUserAccounts.vue'

// หน้าเพจของนักศึกษาทั้งหมด
import HomepageStudent from '../page/StudentPage/Homepage.vue'
import BookAppointment from '../page/StudentPage/BookAppointment.vue'


const routes = [
    {
      path: '/',
      name: 'landingpage',
      component: landingpage
    },
    {
      path: '/admin',
      children: [
        {path: '/loginadmin', name: "loginadmin", component: LoginAdmin},
        {path: '/homepageAdmin', name: "homepageAdmin", component: HomepageAdmin},
        {path: '/loginrights', name: "loginrights", component: LoginRights},
        {path: '/manageuseraccounts', name: "manageuseraccounts", component: ManageUserAccounts}
      ]
    },

    {
      path: '/LoginUser',
      name: 'LoginUser',
      component: LoginUser
    },

    {
      path: '/HomepageStudent',
      name: 'HomepageStudent',
      component: HomepageStudent
    },

    {
      path: '/BookAppointment',
      name: 'BookAppointment',
      component: BookAppointment
    }


]

export default routes