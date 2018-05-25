$fn=100;
difference(){
    union(){
        translate([2,0,0]) cylinder(r=22.5,h=2);
        translate([16,-17,0]) cube([75,34,2]);
    }
}
translate([24,-13,0]) cylinder(r=2,h=5);
translate([86,-13,0]) cylinder(r=2,h=5);
translate([24,13,0]) cylinder(r=2,h=5);
translate([86,13,0]) cylinder(r=2,h=5);

translate([2,-18.5,0]) cylinder(r=2,h=5);
translate([2,18.5,0]) cylinder(r=2,h=5);
