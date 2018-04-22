from printing_models import print_models, show_completed_models 

unprinted_models = ["spaceship","jaeger","anime figure","statue"]
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)
#Very good the printing_models module and functions work perfectly.

##8-16:
import untitled 

magicians = ["mason karsevar","alice karsevar","kieth mosher","tj hooker"]
great_magicians = untitled.make_great(magicians)
untitled.show_magicians(great_magicians)

import untitled as un 

magicians = ["mason karsevar","alice karsevar","kieth mosher","tj hooker"]
new_magicians = un.make_great(magicians)
un.show_magicians(new_magicians)

from untitled import make_great 

magicians = ["mason karsevar","alice karsevar","kieth mosher","tj hooker"]
new_magicians = make_great(magicians)
print(new_magicians)

from untitled import show_magicians as show 

magicians = ["mason karsevar","alice karsevar","kieth mosher","tj hooker"]
show(magicians)

from untitled import * 

magicians = ["mason karsevar","alice karsevar","kieth mosher","tj hooker"]
new_magicians = make_great(magicians)
show_magicians(new_magicians)






