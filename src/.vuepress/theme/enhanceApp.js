// enhanceApp.js
// これだとbuild時にエラーになります
import Vuetify from 'vuetify'
// import 'vuetify.min.css'
// import Vuetify from '../../vuetify'
import '../../../node_modules/vuetify/dist/vuetify.min.css'
// import '../../node_modules/@mdi/font/css/materialdesignicons.css'


export default ({
    Vue,
    options,
    router,
    siteData
}) => {
    Vue.use(Vuetify)
}