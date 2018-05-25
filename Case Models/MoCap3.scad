
$fn=100;
difference(){
    union(){
        translate([-19,0,0]) cube([4,30,10],center=true);
        translate([19,0,0]) cube([4,30,10],center=true);
        translate([19,15,0]) rotate([0,90,0]) cylinder(r=5,h=4,center=true);
        translate([-19,15,0]) rotate([0,90,0]) cylinder(r=5,h=4,center=true);
        translate([0,-13,0]) cube([36,4,10],center=true);
        translate([0,-15,0]) rotate([90,0,0]) cylinder(r=4,h=8);
    }
    union(){
        translate([0,15,0]) rotate([0,90,0]) cylinder(r=2.5,h=50,center=true);
        translate([0,0,0]) rotate([90,0,0]) cylinder(r=2.5,h=50,center=true);
    }
}