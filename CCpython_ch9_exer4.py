##9-10:
from restaurant import Restaurant, IceCreamStand

italian = Restaurant("nino","italian")
italian.describe_restaurant()
italian.open_restaurant()#this command works perfectly.

#let's see if the subclass IceCreamStand works as well.
iscream = IceCreamStand("the fainting goat","deserts")
iscream.describe_restaurant()
iscream.open_restaurant()
iscream.ice_cream_flavors(["vanilla","cherry","salted carmel","chocolate"])
#Event the IceCreamStand() subclass works perfectly.

##9-11:
import user_admin

user1 = user_admin.Administrator("mason","karsevar","data scientist","seattle","hiking")
user1.describe_user()
user1.greet_user()
#These commends from the User2 parent class work perfectly. I need to see 
#if the subclass works perfectly as well.

user1.privileges.privileges = ["managing user data","barring bad actors"]
user1.privileges.show_privileges()
#Sweet these commands worked perfectly!!!
#I can finally move onto the next chapter.

##9-12:
from administrator import Administrator
admin2 = Administrator("alice","karsevar","project manager","san francisco","hiking")
admin2.describe_user()
admin2.greet_user()
admin2.privileges.privileges = ["bar bad actors","delete messages"]
admin2.privileges.show_privileges()
#Sweet everything works perfectly.
