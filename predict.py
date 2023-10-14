import torch
import numpy as np
from torch_geometric.data import Data

# Create data
features = [[-0.25411826,-0.27648264,-0.22558108,-0.29932743,-0.2991588,-0.27068132,-0.30775693,-0.26973268,-0.25100964,-0.30834255,-0.35384533,-0.22567044,-0.30199206,-0.44841027,-0.31270704,-0.18696047,-0.2657766,-0.3512036,-0.28642225,-0.17158231,-0.2635875,-0.24046761,-0.31330124,-0.10656806,-0.2108776,-0.40768352,-0.27332228,-0.24535842,-0.27271768,0.0066714818,-0.20253144,-0.31400403,-0.26570424,-0.41488853,-0.22777586,-0.21833108,-0.31460166,-0.3119624,-0.2708843,-0.15441215,-0.3012037,-0.31171286,-0.17624278,-0.23889962,-0.20307285,-0.19120611,-0.25433794,-0.20339414,-0.2478936,-0.2714565,-0.30306202,-0.26983544,-0.22618802,-0.30219457,-0.3071159,5.154748,-0.27835634,-0.30832532,-0.36052412,-0.24868086,-0.28008085,-0.2066658,-0.24282522,-0.30628508,-0.11459303,-0.24074954,-0.0066513265,-0.22041686,-0.21960883,0.020564415,-0.14265715,-0.25561875,-0.2787111,-0.1535271,-0.18221192,-0.24385606,-0.27006963,-0.28775844,-0.18463156,-0.22933884,-0.25203356,-0.22158015,-0.27420542,-0.45522183,-0.27628207,-0.1980786,-0.18796468,-0.36208272,-0.23703751,-0.2379717,-0.30730015,-0.2643376,-0.27241588,-0.09903266,-0.117616855,-0.24696544,-0.31289217,-0.22342491,-0.2382084,-0.27272186,-0.23367454,-0.30474883,-0.27394682,-0.30140916,-0.22025442,-0.1109369,-0.2607943,-0.23975025,-0.15297316,-0.2923237,5.886884,-0.26001918,2.9047039,-0.2430991,-0.2872089,-0.26692694,-0.27739725,-0.05551477,-0.2976755,-0.27322856,-0.2236998,-0.28437862,-0.20658107,-0.09102673,-0.2557549,-0.21514018,-0.3759032,-0.22383557],
[-0.26257643,-0.27648264,-0.26235026,-0.22984557,-0.2991588,3.9052124,-0.30775693,-0.22906207,-0.25100964,-0.30834255,-0.3702026,-0.22567044,-0.30199206,-0.44841027,0.00082623796,-0.2245749,-0.2657766,-0.34387857,1.0581543,-0.17158231,-0.2635875,-0.24046761,3.148659,-0.21610811,-0.2108776,-0.40768352,-0.27332228,-0.24535842,-0.27271768,-0.20956494,-0.20253144,-0.019696899,3.8532562,-0.41488853,-0.15907234,-0.1641366,0.2063866,-0.3444354,0.03033124,-0.20770384,-0.3012037,0.000977314,-0.17624278,0.10454534,-0.20529027,-0.17583583,-0.25583348,-0.20339414,-0.2478936,-0.2714565,-0.30306202,2.6790884,0.7223678,-0.30219457,-0.27867982,-0.21157545,2.3819778,-0.30568758,-0.36052412,1.2552243,-0.28008085,7.663082,0.2919518,-0.29263577,-0.22610158,-0.24074954,-0.22571905,-0.22041686,-0.21960883,-0.2343117,-0.14265715,-0.25658262,-0.2787111,0.07320977,-0.18221192,-0.24385606,-0.25795153,0.0032205046,-0.18463156,-0.24005078,-0.25203356,-0.23232034,-0.27420542,-0.45522183,-0.27628207,-0.1980786,-0.14749292,-0.36208272,0.7518879,0.84597427,-0.30538926,-0.2643376,-0.27241588,5.1626673,-0.20463425,-0.24696544,-0.31289217,-0.1601608,-0.2382084,-0.27272186,-0.23256432,3.6509273,-0.27394682,-0.30140916,-0.22025442,-0.22342098,-0.2607943,-0.24297728,-0.15297316,1.3926901,-0.21712625,-0.26829532,-0.32283384,-0.046205547,-0.2872089,-0.26692694,-0.27739725,-0.1801908,-0.291936,3.4204106,-0.09649478,2.9629207,-0.22421566,-0.20950909,4.528076,-0.18748155,-0.34549507,-0.22383557],
[-0.25985458,-0.26686466,-0.24163935,-0.29932743,-0.2991588,-0.26492774,-0.30609027,-0.26973268,-0.24471606,-0.2996943,-0.348991,-0.20468172,-0.30199206,-0.44841027,-0.31270704,-0.20516899,-0.2657766,-0.35109743,-0.28642225,-0.10293737,0.047082532,-0.22124788,-0.3070809,-0.15855736,-0.15024833,-0.40768352,-0.27332228,-0.2047359,-0.27271768,-0.1576618,-0.17344971,-0.31400403,-0.26374683,-0.3984041,-0.22777586,-0.21833108,-0.31460166,-0.3432352,-0.2708843,-0.14103697,-0.3012037,-0.2845958,-0.1735154,-0.22301947,-0.19739282,-0.028535374,-0.25583348,-0.17579159,-0.2478936,-0.2714565,-0.30306202,-0.26983544,-0.21980819,-0.27922386,-0.3071159,-0.023219049,-0.27835634,-0.30832532,-0.36052412,-0.24868086,-0.056333456,-0.18762241,-0.24282522,-0.30067384,-0.2178201,-0.23978445,-0.211215,-0.17210323,-0.21960883,-0.20595141,0.08010017,-0.22086494,-0.2787111,-0.11135274,-0.13906665,-0.026514592,-0.27006963,-0.28775844,-0.1797614,-0.20398992,-0.25203356,-0.23232034,-0.21749488,-0.45522183,-0.27628207,0.18349887,-0.1581785,-0.35907084,-0.2267672,-0.23454066,-0.30730015,-0.2643376,-0.25012422,0.16961399,-0.20463425,-0.24696544,-0.31289217,0.17209679,-0.19018792,-0.27272186,-0.23367454,-0.3021591,-0.27249473,-0.294822,-0.20310864,-0.17240249,-0.24052194,-0.23861118,-0.021688275,-0.2923237,1.4409994,-0.26344875,-0.3471427,-0.2430991,-0.2872089,-0.26692694,-0.27739725,-0.14901942,-0.2848714,-0.27322856,-0.22116818,-0.27657762,-0.10644006,-0.20950909,-0.2497442,-0.19290096,-0.3759032,-0.22383557],
[-0.26257643,-0.27648264,-0.26235026,-0.29932743,-0.2991588,-0.27068132,-0.300401,-0.26973268,-0.25100964,-0.3047634,-0.3702026,-0.22567044,-0.30199206,-0.44841027,-0.31270704,-0.2245749,-0.2657766,-0.3512036,-0.28642225,-0.17158231,-0.2635875,-0.24046761,-0.31330124,-0.22326562,-0.2108776,-0.40768352,-0.27332228,-0.24535842,-0.27271768,-0.20956494,-0.20253144,-0.31400403,-0.26570424,-0.41488853,-0.22777586,-0.21833108,-0.31460166,-0.3444354,-0.2708843,-0.20770384,-0.3012037,-0.31171286,-0.17624278,-0.23889962,-0.20529027,-0.19120611,-0.25583348,-0.20339414,-0.2478936,-0.2714565,-0.30306202,-0.26983544,-0.22618802,-0.30219457,-0.3071159,-0.21157545,-0.27835634,-0.30832532,-0.36052412,-0.24868086,-0.28008085,-0.2066658,-0.24282522,-0.30628508,-0.22610158,-0.24074954,4.852047,5.891833,-0.21960883,-0.2343117,-0.14265715,-0.25658262,-0.2787111,-0.1535271,-0.18221192,-0.24385606,-0.27006963,-0.28775844,-0.18463156,-0.24005078,-0.25203356,-0.23232034,-0.27420542,-0.45522183,0.5965205,-0.1980786,4.3585353,-0.36208272,-0.23703751,-0.2379717,-0.30730015,-0.2643376,-0.27241588,-0.23267463,-0.20463425,-0.24696544,-0.31289217,-0.08421743,-0.2382084,-0.27272186,-0.23367454,-0.30474883,-0.2609256,-0.30140916,-0.20962633,-0.22342098,-0.2607943,-0.24297728,-0.15297316,-0.2923237,-0.21712625,-0.26829532,-0.3471427,-0.2430991,-0.2872089,-0.26692694,-0.27739725,-0.20451848,-0.2976755,-0.27322856,-0.2236998,-0.28437862,-0.22421566,-0.20950909,-0.2557549,-0.21514018,-0.3712565,-0.22383557],
[-0.23554593,-0.27648264,-0.26235026,-0.29761913,-0.2991588,-0.27068132,-0.30775693,-0.26973268,-0.25100964,-0.30834255,-0.3702026,-0.20665993,-0.30199206,-0.43668818,-0.31270704,-0.2245749,-0.2657766,-0.3512036,-0.28642225,-0.16053577,-0.2635875,-0.24046761,-0.31330124,-0.22326562,-0.2108776,-0.40768352,-0.27332228,-0.19324252,-0.27271768,-0.09223861,-0.1657646,-0.31400403,-0.26570424,-0.4102076,-0.22777586,-0.21833108,-0.31460166,-0.33988914,-0.2708843,-0.20770384,-0.3012037,-0.31171286,-0.02748011,-0.23889962,-0.16864502,-0.19120611,-0.25351754,-0.102889165,-0.2478936,-0.2714565,-0.30306202,-0.26983544,-0.22618802,-0.30219457,-0.3071159,-0.21157545,-0.27835634,-0.30832532,-0.36052412,-0.24868086,-0.28008085,-0.2066658,-0.24282522,-0.30628508,-0.18638894,-0.24074954,-0.22331853,-0.22041686,-0.21960883,-0.2343117,-0.11344714,-0.25658262,-0.2787111,0.08290515,-0.18221192,-0.011305605,-0.27006963,-0.28775844,-0.18463156,-0.24005078,-0.24417117,-0.23232034,-0.27420542,2.2036622,-0.27628207,-0.1980786,-0.043559745,-0.36208272,-0.23703751,-0.2379717,-0.30730015,-0.2643376,-0.27241588,-0.1600745,-0.20463425,-0.24696544,-0.31289217,5.6912317,-0.21381178,-0.27272186,-0.23367454,-0.30474883,-0.27394682,-0.30140916,-0.22025442,-0.22342098,4.067165,-0.24297728,-0.05947357,-0.2923237,-0.21712625,-0.26829532,-0.3471427,-0.2430991,-0.2872089,-0.26692694,-0.27739725,-0.20440842,-0.2976755,-0.27322856,-0.2236998,-0.28437862,-0.2211016,-0.20950909,-0.2557549,-0.21514018,2.6702952,-0.22383557]]
targets = [2, 3, 2, 3, 2]
edges = np.array([(0, 1), (1, 0), (1, 2), (2, 1), (2, 4), (4, 2), (3, 4), (4, 3)])

features = torch.Tensor(features)
targets = torch.Tensor(targets).to(torch.int64)
edges = np.rot90(edges, 1)
edges = torch.Tensor(edges.copy()).to(torch.int64)

data = Data(x=features, edge_index=edges, edge_attr=None, y=targets)