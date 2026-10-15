from pathlib import Path
from lxml import etree
import shutil, re
BASE=Path(__file__).resolve().parents[1]
SRC=BASE/'upstream/giants'; OUT=BASE/'dist/fs25'; OUT.mkdir(parents=True,exist_ok=True)
for f in SRC.glob('*.xsd'): shutil.copy2(f,OUT/f.name)
NS='http://www.w3.org/2001/XMLSchema'; X=lambda name:'{%s}%s'%(NS,name)
root=etree.parse(str(SRC/'vehicle.xsd')); doc=root.getroot(); ns={'xs':NS}
vehicle=doc.xpath('./xs:element[@name="vehicle"]',namespaces=ns)[0]
allnode=vehicle.find('./'+X('complexType')+'/'+X('all'))
def elem(parent,name,typ=None,occ='0',maxocc='1',docstr=None):
    attrs={'name':name,'minOccurs':occ,'maxOccurs':maxocc}
    if typ: attrs['type']=typ
    e=etree.SubElement(parent,X('element'),**attrs)
    if docstr:
        a=etree.SubElement(e,X('annotation')); etree.SubElement(a,X('documentation')).text=docstr
    return e
def complex_elem(parent,name,attrs={},children=[],repeat='1',choice=False):
    e=elem(parent,name,maxocc=repeat); ct=etree.SubElement(e,X('complexType'))
    if children:
        seq=etree.SubElement(ct,X('choice') if choice else X('sequence'),minOccurs='0',maxOccurs='unbounded' if choice else '1')
        for c in children: complex_elem(seq,*c) if isinstance(c,tuple) else elem(seq,c)
    for k,v in attrs.items(): etree.SubElement(ct,X('attribute'),name=k,type=v)
    return e
s='xs:string'; b='xs:boolean'; f='xs:float'; i='xs:int'
# README-derived definitions. The source documentation is incomplete; non-specified values stay strings.
objectattrs={k:(b if k in ['visibilityActive','visibilityInactive','compoundChildActive','compoundChildInactive','sharedShaderParameter','interpolation'] else f if k in ['massActive','massInactive','interpolationTime'] else s) for k in 'node rotationActive rotationInactive translationActive translationInactive scaleActive scaleInactive visibilityActive visibilityInactive shaderParameter shaderParameterActive shaderParameterInactive sharedShaderParameter interpolation interpolationTime massActive massInactive centerOfMassActive centerOfMassInactive compoundChildActive compoundChildInactive parentNodeActive parentNodeInactive rigidBodyTypeActive rigidBodyTypeInactive'.split()}
clickattrs={k:(b if k in ['alignToCamera','invertX','invertZ'] else f if k in ['animMaxLimit','animMinLimit','blinkSpeedScale','foldMaxLimit','foldMinLimit','forcedStateValue','direction','scaleOffset','size'] else s) for k in 'alignToCamera animMaxLimit animMinLimit animName blinkSpeedScale foldMaxLimit foldMinLimit forcedStateValue direction iconType invertX invertZ node scaleOffset size type linkNode rotation translation'.split()}
buttonattrs={k:(f if k in ['animMaxLimit','animMinLimit','foldMaxLimit','foldMinLimit','forcedStateValue','direction','range'] else s) for k in 'animMaxLimit animMinLimit animName foldMaxLimit foldMinLimit forcedStateValue direction input range refNode type'.split()}
controlattrs={'negText':s,'posText':s,'analog':b,'analogSpeed':f,'allowsSaving':b,'enabled':b}
trigattrs={k:(f if k in ['width','height','length'] else s) for k in 'node linkNode filename rotation translation width height length'.split()}
# Named types make recursive controls reusable and provide attribute autocomplete.
def named(name,attrs={},children=[]):
    ct=etree.SubElement(doc,X('complexType'),name=name)
    if children:
        choice=etree.SubElement(ct,X('choice'),minOccurs='0',maxOccurs='unbounded')
        for n,t in children: elem(choice,n,t,maxocc='unbounded')
    for k,t in attrs.items(): etree.SubElement(ct,X('attribute'),name=k,type=t)
    return ct
named('MGS_IC_ObjectChange',objectattrs)
named('MGS_IC_ClickPoint',clickattrs)
named('MGS_IC_Button',buttonattrs)
named('MGS_IC_Animation',{'initTime':f,'name':s,'speedScale':f})
named('MGS_IC_Function',{'name':s},[('attacherJoint','MGS_IC_AttacherJoint')])
named('MGS_IC_AttacherJoint',{'indices':s})
named('MGS_IC_Restriction',{'indices':s,'name':s})
named('MGS_IC_Restrictions',{},[('restriction','MGS_IC_Restriction')])
named('MGS_IC_DashboardState',{'rotation':s,'scale':s,'translation':s,'value':s,'visibility':b})
dashfields='activeTime animName baseColor displayType doInterpolation emissiveScale emitColor font fontThickness groups hasNormalMap hiddenColor idleValue intensity interpolationSpeed maxRot maxValueAnim maxValueRot maxValueSlider minRot minValueAnim minValueRot minValueSlider node numberColor numbers onICActivate onICDeactivate precision raiseTime rotAxis textAlignment textColor textMask textScaleX textScaleY textSize valueType'.split()
named('MGS_IC_Dashboard',{k:(b if k in ['doInterpolation','hasNormalMap','onICActivate','onICDeactivate'] else s) for k in dashfields},[('state','MGS_IC_DashboardState')])
named('MGS_IC_DependingDashboards',{k:(b if k in ['dashboardActive','dashboardInactive'] else s) for k in 'animName dashboardActive dashboardInactive dashboardValueActive dashboardValueInactive node numbers'.split()})
named('MGS_IC_DependingMovingPart',{'isInactive':b,'node':s})
named('MGS_IC_DependingMovingTool',{'isInactive':b,'node':s})
named('MGS_IC_DependingInteractiveControl',{'index':i,'minLimit':f,'maxLimit':f})
named('MGS_IC_SoundModifier',{'indoorFactor':f,'delayedSoundAnimationTime':f,'name':s})
named('MGS_IC_Control',controlattrs,[(n,'MGS_IC_'+t) for n,t in [('clickPoint','ClickPoint'),('button','Button'),('animation','Animation'),('function','Function'),('configurationsRestrictions','Restrictions'),('dashboard','Dashboard'),('dependingDashboards','DependingDashboards'),('dependingMovingPart','DependingMovingPart'),('dependingMovingTool','DependingMovingTool'),('dependingInteractiveControl','DependingInteractiveControl'),('soundModifier','SoundModifier'),('objectChange','ObjectChange')]])
named('MGS_IC_OutdoorTrigger',trigattrs)
named('MGS_IC_Controls',{},[('outdoorTrigger','MGS_IC_OutdoorTrigger'),('interactiveControl','MGS_IC_Control')])
named('MGS_IC_Configuration',{},[('interactiveControls','MGS_IC_Controls'),('objectChange','MGS_IC_ObjectChange')])
named('MGS_IC_Configurations',{},[('interactiveControlConfiguration','MGS_IC_Configuration')])
named('MGS_IC_ClickIcon',{'blinkSpeed':f,'filename':s,'name':s,'node':s})
named('MGS_IC_Registers',{},[('clickIcon','MGS_IC_ClickIcon')])
named('MGS_IC_Root',{},[('interactiveControls','MGS_IC_Controls'),('interactiveControlConfigurations','MGS_IC_Configurations'),('registers','MGS_IC_Registers')])
elem(allnode,'interactiveControl','MGS_IC_Root',docstr='Interactive Control third-party extension. Requires Interactive Control mod.')
# Vehicle Years uses storeData/year, not storeData/specs/year.
store=doc.xpath('./xs:element[@name="vehicle"]/xs:complexType/xs:all/xs:element[@name="storeData"]',namespaces=ns)[0]
store_all=store.find('./'+X('complexType')+'/'+X('all'))
elem(store_all,'year','xs:int',docstr='Vehicle model year.')

# Exhaust extension is supplied by a third-party specialization. Accept its
# content without weakening validation of the surrounding motorized element.
motorized=doc.xpath('./xs:element[@name="vehicle"]/xs:complexType/xs:all/xs:element[@name="motorized"]',namespaces=ns)[0]
motor_choice=motorized.find('./'+X('complexType')+'/'+X('choice'))
exhaust=elem(motor_choice,'exhaustExtension')
exhaust_type=etree.SubElement(exhaust,X('complexType'))
exhaust_sequence=etree.SubElement(exhaust_type,X('sequence'),minOccurs='0')
etree.SubElement(exhaust_sequence,X('any'),minOccurs='0',maxOccurs='unbounded',processContents='lax')
etree.SubElement(exhaust_type,X('anyAttribute'),processContents='lax')

# Dashboard RPM values are used by mod-specific dashboard implementations.
for dashboard in doc.xpath('.//xs:element[@name="dashboard"]',namespaces=ns):
    dashboard_type=dashboard.find('./'+X('complexType'))
    if dashboard_type is not None and not dashboard_type.xpath('./xs:attribute[@name="minRpm"]',namespaces=ns):
        etree.SubElement(dashboard_type,X('attribute'),name='minRpm',type='xs:float')

# MGS DRL Color configuration.
drl=elem(allnode,'mgsDrlColor',docstr='MGS DRL color configuration.')
drl_type=etree.SubElement(drl,X('complexType'))
for key,kind in [('node',s),('colorConfiguration',s),('typeConfiguration',s),('staticIndex',i),('hueIndex',i),('cycleSpeed',f)]:
    etree.SubElement(drl_type,X('attribute'),name=key,type=kind)
# Add IC animation-part attributes only where the original schema defines vehicle/animations/animation/part.
# Avoid broad changes to unrelated animation parts; this remains a follow-up until exact paths are verified.
root.write(str(OUT/'vehicle.xsd'),encoding='UTF-8',xml_declaration=True,pretty_print=False)
print('Built',len(list(OUT.glob('*.xsd'))),'schemas')
