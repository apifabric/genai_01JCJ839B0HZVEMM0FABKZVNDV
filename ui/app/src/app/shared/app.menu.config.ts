import { MenuRootItem } from 'ontimize-web-ngx';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { GuestCardComponent } from './Guest-card/Guest-card.component';

import { HotelCardComponent } from './Hotel-card/Hotel-card.component';

import { MaintenanceRequestCardComponent } from './MaintenanceRequest-card/MaintenanceRequest-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { ReservationCardComponent } from './Reservation-card/Reservation-card.component';

import { ReservationServiceCardComponent } from './ReservationService-card/ReservationService-card.component';

import { RoomCardComponent } from './Room-card/Room-card.component';

import { ServiceCardComponent } from './Service-card/Service-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'Guest', name: 'GUEST', icon: 'view_list', route: '/main/Guest' }
    
        ,{ id: 'Hotel', name: 'HOTEL', icon: 'view_list', route: '/main/Hotel' }
    
        ,{ id: 'MaintenanceRequest', name: 'MAINTENANCEREQUEST', icon: 'view_list', route: '/main/MaintenanceRequest' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'Reservation', name: 'RESERVATION', icon: 'view_list', route: '/main/Reservation' }
    
        ,{ id: 'ReservationService', name: 'RESERVATIONSERVICE', icon: 'view_list', route: '/main/ReservationService' }
    
        ,{ id: 'Room', name: 'ROOM', icon: 'view_list', route: '/main/Room' }
    
        ,{ id: 'Service', name: 'SERVICE', icon: 'view_list', route: '/main/Service' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    EmployeeCardComponent

    ,GuestCardComponent

    ,HotelCardComponent

    ,MaintenanceRequestCardComponent

    ,PaymentCardComponent

    ,ReservationCardComponent

    ,ReservationServiceCardComponent

    ,RoomCardComponent

    ,ServiceCardComponent

];