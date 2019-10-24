import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class RequestInstallationService{

    constructor(){}


    getInstallationRequests() {
        const url = `${API_URL}/api/request/`;
        return axios.get(url).then(response => response.data);
    }

    getInstallationRequest(pk) {
        const url = `${API_URL}/api/request/${pk}`;
        return axios.get(url).then(response => response.data);
    }

    createInstallationRequest(request){
        const url = `${API_URL}/api/request/`;
        return axios.post(url,request);
    }
    updateInstallationRequest(request){
        const url = `${API_URL}/api/request/${request.pk}`;
        return axios.put(url,request);
    }
}
