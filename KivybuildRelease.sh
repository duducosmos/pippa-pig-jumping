#!/bin/bash
echo "Script de compilacao e instalacao de apk"
echo "Por Eduardo S. Pereira"
echo " "
echo "Entrando no diretorio do python-for-android"
echo " "
cd ../kivy/python-for-android/dist/default
gamefolder=PippaPigJumping10
gamePackage=com.jds.pippapig11
gameName="Pippa Pig Jump"
gameVersion=2.0.1
numericalVersion=12
gameApkName=PippaPigJump
echo "Vesion of the game: $gameVersion - Numerica $numericalVersion"
python build.py \
--dir /media/Dados/projects/ProjetosJava/GAMES/$gamefolder/src/ \
--package $gamePackage \
--name "$gameName" \
--minsdk 9 \
--sdk 9 \
--icon /media/Dados/projects/ProjetosJava/GAMES/$gamefolder/src/images/icon.png \
--presplash /media/Dados/projects/ProjetosJava/GAMES/$gamefolder/src/images/jabuticabaLogo.png \
--version $gameVersion --numeric-version $numericalVersion release

echo "Compilacao Finalizada, deseja continuar para a Instalacao (y/n)"
read continua

if test $continua = "y"
then
echo "Movendo e instalando o arquivo compilado"
echo "Moving Apk"
mv ./bin/$gameApkName-$gameVersion-release-unsigned.apk \
   /media/Dados/projects/ProjetosJava/GAMES/$gamefolder/APKs/$gameApkName_unalign.apk
cd /media/Dados/projects/ProjetosJava/GAMES/$gamefolder/APKs/
rm $gameApkName.apk
echo "Sing Apk"
/usr/lib/jvm/java-6-oracle/bin/jarsigner  -verbose -keystore ./KeyReleaseStore.keystore -storepass pass -keypass keypass ./$gameApkName_unalign.apk nameKeystore
echo "Verify Sing"
/usr/lib/jvm/java-6-oracle/bin/jarsigner -verify -verbose -certs $gameApkName_unalign.apk
echo "Align APK"
zipalign -f -v 4 $gameApkName_unalign.apk $gameApkName.apk
echo "Verify Align"
zipalign -c -v 4 $gameApkName.apk
echo "Trying to install into Device"
adb install -r $gameApkName.apk
fi
