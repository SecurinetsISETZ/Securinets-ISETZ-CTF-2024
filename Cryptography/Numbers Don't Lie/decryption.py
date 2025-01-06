from sympy import mod_inverse


c = 4343617797788293378943826336528524550400358887222787715212707057150343302833958324858886148768393581613778615615619513412167896286916094216235623356288729633624502477435796845050902434922446143045876969428699337155951555940354529071472003607727587158998465527137674150542923885875467290455273972001261929364650321609356824800855654361448800567611710910476044130138186204945748676836735858204961765343802795478642142652530987998058099818172406569388014416508503387910511584878640898056879710187346009278396545312594794820597592397933684273847842992397499296948579277678223301843077762162129579087381105110252065692791
e = 65537
n = 25123858645694187518208107836050633422418985958322028829841518734709455464358584837344126879204480153344920453235729232358411794335268215661947363693399408947394339310686688691621986447160110094219918427936020532119624448935130852074264491903743655566470037438923831081598935691243083998651168913840041197931272150974124794057425337564932004298723159730235152878926257166830359997845878460483207907637096270773771790740800811878038578230472767375349640007970773246035810211025978866979907755688728275769345052739175234101897664399432709975941118537525133827069657039657022661271347771407285547588087500413839327228287

phi_n = n - 1 

d = mod_inverse(e, phi_n)

m = pow(c, d, n)

decrypted_message = bytes.fromhex(hex(m)[2:]).decode('utf-8')


print(f"Decrypted message: {decrypted_message}")
