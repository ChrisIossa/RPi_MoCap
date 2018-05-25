$fn=100;
difference(){
    union(){
        translate([2,0,0]) cylinder(r=22.5,h=10);
        translate([16,-17,0]) cube([75,34,10]);
    }
    union(){
        translate([2,0,1]) cylinder(r=20.5,h=10);
        translate([2,0,-1]) cylinder(r=19,h=11);
        translate ([69.5,10,2]) cube(12);
        translate ([42.3,10,2]) cube(8);
        translate ([30,10,2]) cube(8);
        translate([0,-9,2]) cube([100,18,10]);
        translate([22.5,-15.5,2]) cube([65.7,31,10]);
    }
}
# translate([90.7,17.8,0]) rotate([0,0,180]) import("RPi0.stl");
union(){
    translate([26.4,11.4,3]) cylinder(r=1.1,h=5,center=true);
    translate([26.4,-11.5,3]) cylinder(r=1.1,h=5,center=true);
    translate([84.4,11.4,3]) cylinder(r=1.1,h=5,center=true);
    translate([84.4,-11.5,3]) cylinder(r=1.1,h=5,center=true);
}
difference(){
    union(){
        translate([100,-13,5]) rotate([90,0,0]) cylinder(r=5,h=4);
        translate([100,17,5]) rotate([90,0,0]) cylinder(r=5,h=4);
        translate([90,13,0]) cube([10,4,10]);
        translate([90,-17,0]) cube([10,4,10]);
    }
    {
        translate([100,0,5]) rotate([90,0,0])cylinder(r=2.5,h=50,center=true);
    }
}