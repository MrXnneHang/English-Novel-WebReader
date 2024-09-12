import axios from 'axios';

// 创建Axios实例
axios.defaults.baseURL = 'http://127.0.0.1:5000';
export default axios;
// // 请求拦截器
// instance.interceptors.request.use(
//   config => {
//     // 在请求发送之前做一些处理,例如添加token等
//     return config;
//   },
//   error => {
//     // 处理请求错误
//     return Promise.reject(error);
//   }
// );

// // 响应拦截器
// instance.interceptors.response.use(
//   response => response,
//   error => {
//     // 处理响应错误
//     return Promise.reject(error);
//   }
// );