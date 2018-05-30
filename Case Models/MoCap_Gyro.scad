$fn=100;
difference(){
    union(){
        translate([2,0,0]) cylinder(r=22.5,h=26);
        translate([16,-17,0]) cube([75,34,26]);
    }
    union(){
        translate([2,0,1]) cylinder(r=20.5,h=26);
        translate([2,0,-1]) cylinder(r=19,h=27);
        translate ([69.5,10,2]) cube(12);
        translate ([42.3,10,2]) cube(8);
        translate ([30,10,2]) cube(8);
        translate([0,-9,2]) cube([100,18,10]);
        translate([22.5,-15.5,2]) cube([65.7,31,26]);
    }
}
// translate([90.7,17.8,0]) rotate([0,0,180]) import("RPi0.stl");
// translate([90.7,17.8,11.5]) rotate([0,0,180]) import("RPi0.stl");
//# translate([0,0,27]) rotate([0,180,180]) import("MoCap2_Gyro.stl");
// translate([115,0,10]) rotate([0,0,90]) import("MoCap3.stl");
// translate([165,0,10]) rotate([0,270,0]) import("MoCap4.stl");

union(){
    translate([26.4,11.4,3]) cylinder(r=1.1,h=5,center=true);
    translate([26.4,-11.5,3]) cylinder(r=1.1,h=5,center=true);
    translate([84.4,11.4,3]) cylinder(r=1.1,h=5,center=true);
    translate([84.4,-11.5,3]) cylinder(r=1.1,h=5,center=true);
}
difference(){
    union(){
        translate([100,-13,10]) rotate([90,0,0]) cylinder(r=5,h=4);
        translate([100,17,10]) rotate([90,0,0]) cylinder(r=5,h=4);
        translate([90,13,5]) cube([10,4,10]);
        translate([90,-17,5]) cube([10,4,10]);
    }
    {
        translate([100,0,10]) rotate([90,0,0])cylinder(r=2.5,h=50,center=true);
    }
}