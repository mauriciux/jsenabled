project_name=jsenabled
cur_dir=$(shell pwd)
lib_dir=$(shell (cd ../lib && pwd))
src_dir=$(shell (cd ../src && pwd))
du_dir=$(shell (cd ../src/double-underscore && pwd))
googleapp_dir=${lib_dir}/google_appengine
ga_htdocs_dir=${googleapp_dir}/${project_name}
source_svn=https://jsenabled.googlecode.com/svn/trunk/

empty:

update_du:
	(cd ${googleapp_dir} && ./appcfg.py update ${du_dir})

get_du_logs:
	#(cd ${googleapp_dir} && ./appcfg.py request_logs ${du_dir} ../../du_logs.txt && cat ../../du_logs.txt >> ../../log/du_logs.txt && rm ../../du_logs.txt)
	(cd ${googleapp_dir} && ./appcfg.py -a request_logs ${du_dir} ../../log/du_logs.txt)

clean_htdocs:
	rm -rf ${ga_htdocs_dir};

build_htdocs:
	mkdir ${ga_htdocs_dir}
	cp -r ${src_dir}/* ${ga_htdocs_dir}

refresh_htdocs:
	make clean_htdocs
	make build_htdocs

start_debug:
	make refresh_htdocs
	(cd ${googleapp_dir} && ./dev_appserver.py ${project_name}/ --address=0.0.0.0)

make_min_dir:
	if [ -d ${ykjs_dir} ]; then make clean; fi
	svn export ${source_svn} ${ykjs_dir}

compress:
	make make_min_dir
	for ii in `find ${ykjs_dir} -mindepth 1 -type d -name "demo"`;do rm -rf $$ii;done 
	rev=`svn info ${source_svn} | awk '/^Revision: /{print $$2}'`;\
	for ii in `find ${ykjs_dir} -mindepth 1 -type f -name "*.js"`;\
		do vv=`awk -F":" '/^ \* version:/{sub("\r$$", "");print $$2}' $$ii`;\
	  ii1=$${ii%.js};\
		java -jar ${jar_dir} --charset utf8 -v -o $${ii1}_$${vv}.tmp.js $$ii;\
		sed '/^ \* revision:$$/c\ * revision:'$$rev $${ii1}_$${vv}.tmp.js > $${ii1}_$${vv}.js;\
		rm $$ii;\
		rm $${ii1}_$${vv}.tmp.js;\
	done;\
	for ii in `find ${ykjs_dir} -mindepth 1 -type f -name "*.css"`;\
		do vv=`awk -F":" '/^ \* version:/{sub("\r$$", "");print $$2}' $$ii`;\
	  ii1=$${ii%.css};\
		sed '/^ \* revision:$$/c\ * revision:'$$rev $$ii > $${ii1}_$${vv}.tmp.css;\
		java -jar ${jar_dir} --charset utf8 -v -o $${ii1}_$${vv}.css $${ii1}_$${vv}.tmp.css;\
		rm $$ii;\
		rm $${ii1}_$${vv}.tmp.css;\
	done;
	echo
	echo All file compressed to :
	echo ${ykjs_dir}
