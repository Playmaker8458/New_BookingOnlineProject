// หน้่าเพจหลัก
import landingpage from '../page/landingpage.vue'

// layout
import AdminLayout from '../page/AdminPage/AdminLayout.vue'

// หน้า Login ของผู้ดูแลระบบ และผู้ใช้ทั้ง 2 กลุ่ม [นักศึกษา และ อาจารย์]
import LoginAdmin from '../page/LoginAdmin.vue'
import LoginUser from '../page/LoginUser.vue'

// หน้า รอยืนยันสิทธิ์การเข้าสู่ระบบ
import LoginVerification from '../page/LoginVerification.vue'

// หน้าเพจของผู้ดูแลระบบทั้งหมด
import HomepageAdmin from '../page/AdminPage/Homepage.vue'
import LoginRights from '../page/AdminPage/LoginRights.vue'
import ManageUserAccounts from '../page/AdminPage/ManageUserAccounts.vue'

// หน้าเพจของนักศึกษาทั้งหมด
import HomepageStudent from '../page/StudentPage/Homepage.vue'
import BookAppointment from '../page/StudentPage/BookAppointment.vue'
import ManageQueueStudent from '../page/StudentPage/Managequeue.vue'
import RescheduleAppointmentStudent from '../page/StudentPage/RescheduleAppointment.vue'

// หน้าเพจของอาจารย์ทั้งหมด
import HomepageAdvisor from '../page/AdvisorPage/Homepage.vue'
import ConsultationTimeSlot from '../page/AdvisorPage/ConsultationTimeSlot.vue'
import ManageQueueAdvisor from '../page/AdvisorPage/ManageQueue.vue'
import RescheduleAppointmentAdvisor from '../page/AdvisorPage/RescheduleAppointment.vue'
import ConsultationTimeControl from '../page/AdvisorPage/ConsultationTimeControl.vue'


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
        {path: 'loginadmin', name: "loginadmin", component: LoginAdmin},
        {
          path: 'homepageAdmin',
          name: 'homepageAdmin',
          component: HomepageAdmin,
          meta: { requiresAuth: true }
        },
        { path: 'loginrights', name: "loginrights", component: LoginRights },
        { path: 'manageuseraccounts', name: "manageuseraccounts", component: ManageUserAccounts }
      ]
    },

    {
      path: '/LoginUser',
      name: 'LoginUser',
      component: LoginUser
    },
    {
      path: '/LoginVerification',
      name: 'LoginVerification',
      component: LoginVerification
    },
    {
      path : '/Students',
      children :[
        {path: '/HomepageStudent', name: 'HomepageStudent', component: HomepageStudent},
        {path: '/BookAppointment', name: 'BookAppointment', component: BookAppointment},
        {path: '/ManageQueueStudent', name: 'ManageQueueStudent', component: ManageQueueStudent},
        {path: '/RescheduleAppointmentStudent', name: 'RescheduleAppointmentStudent', component: RescheduleAppointmentStudent},
      ]
    },
    {
      path: '/Advisor',
      children:[
        {path: '/HomepageAdvisor', name: 'HomepageAdvisor', component: HomepageAdvisor},
        {path: '/ConsultationTimeSlot', name: 'ConsultationTimeSlot', component: ConsultationTimeSlot},
        {path: '/ManageQueueAdvisor', name: 'ManageQueueAdvisor', component: ManageQueueAdvisor},
        {path: '/RescheduleAppointmentAdvisor', name: 'RescheduleAppointmentAdvisor', component: RescheduleAppointmentAdvisor},
        {path: '/ConsultationTimeControl', name: 'ConsultationTimeControl', component: ConsultationTimeControl}
      ]
    }
]

export default routes